def rowify_binary_tree(node, level=0):
    """
    Proper implementation should be as follows:

    node_array = []
    node_array = rowify_binary_tree(root)

    Turns a binary tree into a list of lists, with each inner list containing every node at a particular depth from the root. Nodes will be in order, but null roots will not be taken into account.

    :param node: Represents a node in a binary tree. Contains a self.val, indicating data contents, and two pointers, self.left and self.right, which are pointed at the children.
    :param level: Indicates which "row" a node is on. Root is at row 0, root.child is at row 1, etc.
    :return: None, but THERE MUST EXIST AN EMPTY LIST WITH THE NAME node_array IN THE PROGRAM PRIOR TO CALL
    """
    nonlocal node_array
    if not node:
        return
    if len(node_array) <= level:
        node_array.append([])
    node_array[level].append(node.val)
    rowify_binary_tree(node.left, level + 1)
    rowify_binary_tree(node.right, level + 1)
    return
