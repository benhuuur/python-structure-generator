from AST.AST_handler import AST_handler
from JSON.JSON_serializer import JSON_serializer

# tree = AST_handler.get_AST("examples\\GPT_test.py")
tree = AST_handler.get_AST("examples\\test.py")
# tree = AST_handler.get_AST("examples\\test_class.py")

# AST_handler.print_tree(tree)

classes = AST_handler.get_classes(tree.body)
print("\n")


dict_classes = list()
for current_class in classes:
    dict_classes.append(current_class.to_dict())

JSON_serializer.save_to_json(data=dict_classes, filename="class.json")
