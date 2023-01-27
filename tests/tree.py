import os


def remove_common_root(tree_strings):
    common_prefix = os.path.commonprefix(tree_strings)
    tree_strings = [string.replace(common_prefix, "") for string in tree_strings]
    return tree_strings


# test example
tree_strings = [
    "another.module.this.that",
    "another.module.this.here",
    "another.module.main",
]
print(remove_common_root(tree_strings))
