# Start with some designs that need to be printed.
def printing(*topping):
    unprinted_designs = []
    completed_models = []
    print(type(unprinted_designs))
    print(topping)
    for i in topping:

        unprinted_designs.append(i)


    #simulate printing each design, until none are left.
    #Move each design to completed_models printing.

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

    #Display all completed models.
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

    print(type(completed_model))
    print(type(current_design))
    print(type(completed_models))
