from skill_tree.tree import TreeWalker

if __name__ == '__main__':
    walker = TreeWalker("data", "scheme", "Scheme", ignore_keywords=True)
    walker.walk()
