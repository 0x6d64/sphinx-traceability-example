import graphviz

def hello_check(app, doctree):
    env = app.builder.env

    traceability_data = env.traceability_collection


    print("hello!")
    print(traceability_data)

def export_as_dotfile(app, doctree):
    env = app.builder.env
    traceability_data = env.traceability_collection
    dotfile_path = app.config.traceability_dot_export_path
    dot = graphviz.Digraph()
    dot.graph_attr['rankdir'] = 'LR'

    for item_id in traceability_data.iter_items():
        item = traceability_data.get_item(item_id)
        item_id = item.get_id()
        dot.node(item_id)
        for relation in item.iter_relations():
            print("relation " + relation)
            for target_id in item.iter_targets(relation, explicit=True, implicit=False, sort=False):
                dot.edge(item_id, target_id, label=relation)

    print(dot.source)
    dot.render(dotfile_path, view=True)
