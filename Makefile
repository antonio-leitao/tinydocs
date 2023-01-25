help:
	@echo "\nAvailable commnads:"
	@echo ">> init : Initiates python environment" | sed 's/^/   /'
	@echo ">> clean : removes all pycaches" | sed 's/^/   /'
	@echo ">> commit : commits all changes to git" | sed 's/^/   /'
	@echo ">> release : Updates version, builds and releases package to Pypy" | sed 's/^/   /'

init: 
	@pip install pip-chill
	@pip install --upgrade twine

clean:
	@find . -name \*.pyc -delete
	@find . -type d -name "__pycache__" -delete

commit:
	@git add -A
	@DESCRIPTION=$$(gum write --width 60 --height 6 --base.margin "1 1" --cursor.foreground 31 --placeholder "Details of this change (CTRL+D to finish)");\
	gum confirm --selected.background 31 "Commit changes?" && git commit -m "$$DESCRIPTION"
	@git push origin master


changelog:
	@TAG=`git describe --abbrev=0 --tags 2>/dev/null`; \
	if [ -z "$$TAG" ]; then \
		TAG=`git rev-list --max-parents=0 HEAD`; \
	fi; \
	COMMITS=`git log --oneline $$TAG..HEAD | grep -v -e "Typo" -e "Typos" -e "Bugfix"`; \
	if [ -z "$$COMMITS" ]; then \
		echo "No new commits since the last tag."; \
		exit 0; \
	fi; \
	echo "## Changes since $$TAG" >> CHANGELOG.md; \
	echo "" >> CHANGELOG.md; \
	while read -r COMMIT; do \
		SHA=`echo $$COMMIT | awk '{print $$1}'`; \
		DESCRIPTION=`echo $$COMMIT | sed 's/^[^ ]* //'`; \
		echo "* $$SHA: $$DESCRIPTION" >> CHANGELOG.md; \
	done <<< "$$COMMITS"

release:
	@UPDATE=$$(gum choose "Major" "Minor" "Patch" --limit "1" --cursor.margin "0 1" --cursor.foreground "");\
	VERSION=$(shell grep -m 1 version pyproject.toml | tr -s ' ' | tr -d '"' | tr -d "'" | cut -d' ' -f3);\
	IFS=. read major minor patch <<<"$$VERSION";\
	if [ "$$UPDATE" = "Major" ]; then\
        major=$$(( $$major + 1 ));\
		minor=0;\
		patch=0;\
    fi;\
	if [ "$$UPDATE" = "Minor" ]; then\
        minor=$$(( $$minor + 1 ));\
		patch=0;\
    fi;\
	if [ "$$UPDATE" = "Patch" ]; then\
        patch=$$(($$patch + 1));\
    fi;\
	NEW="$$major.$$minor.$$patch";\
	sed -i "" "s/^version = ".*"/version = \"$$NEW\"/" pyproject.toml;\
	git add pyproject.toml;\
	git commit -m "Updated version";\
	python -m build;\
	$(MAKE) changelog;\
	git tag -a $$NEW -m "Release";\
	git push origin master --tags;\
	gh release create $$NEW -F CHANGELOG.md --title "Jet v$$NEW";\
	twine upload dist/*;\
	rm CHANGELOG.md

retag:
	@TAG=$$(gum input --placeholder "version to drop");\
	gum confirm --selected.background 31 "Are you sure?" && git tag -d $$TAG && git push --delete origin $$TAG;\
	git add -A;\
	git commit -m "Bugfix";\
	git tag -a $$TAG -m "Pre-Release";\
	git push origin master --tags

