knowledge_base = {
    "Facts": [
        {"proposition": "colorful wings", "positive": True},
        {"proposition": "feeds on nectar", "positive": True},
        {"proposition": "active during the day", "positive": True},
        {"proposition": "dull-colored wings", "positive": True},
        {"proposition": "active at night", "positive": True},
        {"proposition": "attracted to light", "positive": True},
        {"proposition": "yellow", "positive": True},
        {"proposition": "black stripes", "positive": True},
        {"proposition": "buzzing sound", "positive": True},
        {"proposition": "thin waist", "positive": True},
        {"proposition": "small size", "positive": True},
        {"proposition": "lives in colonies", "positive": True},
        {"proposition": "carries food", "positive": True},
        {"proposition": "eats wood", "positive": True},
        {"proposition": "red shell with black spots", "positive": True},
        {"proposition": "long legs", "positive": True},
        {"proposition": "jumps high", "positive": True},
        {"proposition": "chirping sound", "positive": True},
        {"proposition": "long transparent wings", "positive": True},
        {"proposition": "large compound eyes", "positive": True},
        {"proposition": "thin body", "positive": True},
        {"proposition": "bites humans", "positive": True},
        {"proposition": "oval body", "positive": True},
        {"proposition": "fast-moving", "positive": True},
        {"proposition": "eight legs", "positive": True},
        {"proposition": "web-building behavior", "positive": True},
        {"proposition": "emits light", "positive": True},
        {"proposition": "camouflaged body", "positive": True},
        {"proposition": "slow movement", "positive": True},
        {"proposition": "hard shell", "positive": True},
        {"proposition": "feeds on plants or scavenger", "positive": True},
        {"proposition": "long forelegs", "positive": True},
        {"proposition": "triangular head", "positive": True},
        {"proposition": "number of bites > 5", "positive": True},
        {"proposition": "wingspan > 1.5 cm", "positive": True},
        {"proposition": "colony size > 50", "positive": True},
        {"proposition": "yellow", "positive": False},
        {"proposition": "black trips", "positive": False},
        {"proposition": "active at night ", "positive": False},
        {"proposition": "attracted to light", "positive": False}
    ],
    "Rules": [
        {"result": "Butterfly", "condition": [{"proposition": "colorful wings", "positive": True},{"proposition": "feeds on nectar", "positive": True}]},
        {"result": "Butterfly", "condition": [{"proposition": "colorful wings", "positive": True}, {"proposition": "active during the day", "positive": True}]},

        {"result": "Moth", "condition": [{"proposition": "dull-colored wings", "positive": True}, {"proposition": "active at night", "positive": True}]},
        {"result": "Moth", "condition": [{"proposition": "dull-colored wings", "positive": True}, {"proposition": "attracted to light", "positive": True}]},

        {"result": "Bee", "condition": [{"proposition": "yellow", "positive": True}, {"proposition": "black stripes", "positive": True}, {"proposition": "buzzing sound", "positive": True}]},
        {"result": "Bee", "condition": [{"proposition": "yellow", "positive": True}, {"proposition": "black stripes", "positive": True}, {"proposition": "feeds on nectar", "positive": True}]},

        {"result": "Wasp", "condition": [{"proposition": "yellow", "positive": True}, {"proposition": "black stripes", "positive": True}, {"proposition": "buzzing sound", "positive": True}, {"proposition": "thin waist", "positive": True}]},
        {"result": "Wasp", "condition": [{"proposition": "yellow", "positive": True}, {"proposition": "black stripes", "positive": True}, {"proposition": "feeds on nectar", "positive": True}, {"proposition": "thin waist", "positive": True}]},

        {"result": "Ant", "condition": [{"proposition": "small size", "positive": True}, {"proposition": "lives in colonies", "positive": True}]},
        {"result": "Ant", "condition": [{"proposition": "small size", "positive": True}, {"proposition": "carries food", "positive": True}]},

        {"result": "Termite", "condition": [{"proposition": "small size", "positive": True}, {"proposition": "lives in colonies", "positive": True}, {"proposition": "eats wood", "positive": True}]},
        {"result": "Termite", "condition": [{"proposition": "small size", "positive": True}, {"proposition": "carries food", "positive": True}, {"proposition": "eats wood", "positive": True}]},

        {"result": "Ladybug", "condition": [{"proposition": "small size", "positive": True}, {"proposition": "red shell with black spots", "positive": True}]},

        {"result": "Grasshopper", "condition": [{"proposition": "long legs", "positive": True}, {"proposition": "jumps high", "positive": True}]},
        {"result": "Grasshopper", "condition": [{"proposition": "long legs", "positive": True}, {"proposition": "chirping sound", "positive": True}]},

        {"result": "Dragonfly", "condition": [{"proposition": "long transparent wings", "positive": True}, {"proposition": "large compound eyes", "positive": True}]},

        {"result": "Mosquito", "condition": [{"proposition": "thin body", "positive": True}, {"proposition": "buzzing sound", "positive": True}]},
        {"result": "Mosquito", "condition": [{"proposition": "thin body", "positive": True}, {"proposition": "bites humans", "positive": True}]},

        {"result": "Cockroach", "condition": [{"proposition": "oval body", "positive": True}, {"proposition": "fast-moving", "positive": True}]},
        {"result": "Cockroach", "condition": [{"proposition": "oval body", "positive": True}, {"proposition": "active at night", "positive": True}]},

        {"result": "Spider", "condition": [{"proposition": "eight legs", "positive": True}, {"proposition": "web-building behavior", "positive": True}]},

        {"result": "Firefly", "condition": [{"proposition": "dull-colored wings", "positive": True}, {"proposition": "active at night", "positive": True}, {"proposition": "emits light", "positive": True}]},
        {"result": "Firefly", "condition": [{"proposition": "dull-colored wings", "positive": True}, {"proposition": "attracted to light", "positive": True}, {"proposition": "emits light", "positive": True}]},

        {"result": "Stick Insect", "condition": [{"proposition": "camouflaged body", "positive": True}, {"proposition": "slow movement", "positive": True}]},

        {"result": "Beetle", "condition": [{"proposition": "hard shell", "positive": True}, {"proposition": "feeds on plants", "positive": True}]},
        {"result": "Beetle", "condition": [{"proposition": "hard shell", "positive": True}, {"proposition": "scavenger", "positive": True}]},

        {"result": "Praying Mantis", "condition": [{"proposition": "long forelegs", "positive": True}, {"proposition": "triangular head", "positive": True}]},

        {"result": "Ant Colony Leader", "condition": [{"proposition": "small size", "positive": True}, {"proposition": "lives in colonies", "positive": True}, {"proposition": "colony size > 50", "positive": True}]},
        {"result": "Ant Colony Leader", "condition": [{"proposition": "small size", "positive": True}, {"proposition": "carries food", "positive": True}, {"proposition": "colony size > 50", "positive": True}]},

        {"result": "Queen Bee", "condition": [{"proposition": "yellow", "positive": True}, {"proposition": "black stripes", "positive": True}, {"proposition": "buzzing sound", "positive": True}, {"proposition": "wingspan > 1.5", "positive": True}]},
        {"result": "Queen Bee", "condition": [{"proposition": "yellow", "positive": True}, {"proposition": "black stripes", "positive": True}, {"proposition": "feeds on nectar", "positive": True}, {"proposition": "wingspan > 1.5", "positive": True}]},
        
        {"result": "Mosquito Carrier", "condition": [{"proposition": "thin body", "positive": True}, {"proposition": "buzzing sound", "positive": True}, {"proposition": "number of bites > 5", "positive": True}]},
        {"result": "Mosquito Carrier", "condition": [{"proposition": "thin body", "positive": True}, {"proposition": "bites humans", "positive": True}, {"proposition": "number of bites > 5", "positive": True}]},

        {"result": "Housefly", "condition": [{"proposition": "small size", "positive": True}, {"proposition": "buzzing sound", "positive": True}, {"proposition": "yellow", "positive": False}]},
        {"result": "Housefly", "condition": [{"proposition": "small size", "positive": True}, {"proposition": "buzzing sound", "positive": True}, {"proposition": "black trips", "positive": False}]},
        {"result": "Housefly", "condition": [{"proposition": "small size", "positive": True}, {"proposition": "buzzing sound", "positive": True}, {"proposition": "active at night ", "positive": False}]},
        {"result": "Housefly", "condition": [{"proposition": "small size", "positive": True}, {"proposition": "buzzing sound", "positive": True}, {"proposition": "attracted to light", "positive": False}]}
    ]
}
   


def is_fact_known(facts, conclusion):
    for fact in facts:
        if fact == conclusion:
            return True
    return False


def backward_chaining(facts, conclusion):
    if not isinstance(conclusion, list):
        rules = knowledge_base['Rules']
        if is_fact_known(facts, conclusion):
            return True
        for rule in rules:
            if rule['result'] == conclusion:
                if backward_chaining(facts, rule['condition']):
                    return True
    else:
        if len(conclusion) == 0:
            return True
        
        first_condition = conclusion[0]
        remaining_conditions = conclusion[1:]
        if backward_chaining(facts, first_condition):
            return backward_chaining(facts, remaining_conditions)
    
    return False




def is_satisfied(conditions, facts):
    if len(conditions) == 0:
        return True

    first_condition = conditions[0]
    remaining_conditions = conditions[1:]
    if(first_condition in facts):
        return is_satisfied(remaining_conditions,facts)
    else:
        return False


    


def forward_chaining(facts, conclusion):
    rules = knowledge_base['Rules']
    if conclusion in facts:
        return True

    for rule in rules:
        if is_satisfied(rule['condition'], facts) and rule['result'] not in facts:
            facts.append(rule['result'])  
            if rule['result'] == conclusion:
                return True
            else:
                extended_facts = []
                extended_facts.append(rule["result"])
                extended_facts.append(facts)
                return forward_chaining(extended_facts, conclusion)

    return False




import tkinter as tk
from tkinter import ttk

insects_info = [
    {"insect": "Butterfly", "description": "Pollinates flowers, found in gardens."},
    {"insect": "Moth", "description": "Nocturnal pollinator, prefers dark habitats."},
    {"insect": "Bee", "description": "Pollinates flowers, lives in colonies."},
    {"insect": "Wasp", "description": "Predatory, aggressive, and builds paper nests."},
    {"insect": "Ant", "description": "Builds underground nests, highly organized."},
    {"insect": "Termite", "description": "Causes damage to wooden structures."},
    {"insect": "Ladybug", "description": "Feeds on aphids, beneficial for gardens."},
    {"insect": "Grasshopper", "description": "Found in grassy areas, feeds on plants."},
    {"insect": "Dragonfly", "description": "Lives near water, feeds on smaller insects."},
    {"insect": "Housefly", "description": "Common pest, feeds on organic waste."},
    {"insect": "Mosquito", "description": "Transmits diseases, active at night."},
    {"insect": "Cockroach", "description": "Scavenger, found in damp or dark areas."},
    {"insect": "Spider", "description": "Not an insect, traps prey in webs."},
    {"insect": "Firefly", "description": "Nocturnal, bioluminescent."},
    {"insect": "Stick Insect", "description": "Mimics twigs, found in trees."},
    {"insect": "Beetle", "description": "Diverse group, found in various habitats."},
    {"insect": "Praying Mantis", "description": "Predatory, excellent camouflage."},
    {"insect": "Ant Colony Leader", "description": "Directs colony, highly organized."},
    {"insect": "Queen Bee", "description": "Lays eggs, central to hive survival."},
    {"insect": "Mosquito Carrier", "description": "High transmission risk for diseases."}
]

class InsectIdentificationGUI:
    def __init__(self, master):
        self.master = master
        master.title("Insect Identification Expert System")
        master.geometry("800x700")  # Default window size

       
        self.main_frame = ttk.Frame(master, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

      
        self.title_label = ttk.Label(self.main_frame, text="Insect Identification", font=('Arial', 16, 'bold'))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 60))

       
        self.traits_frame = ttk.LabelFrame(self.main_frame, text="Select Observed Traits", padding="10")
        self.traits_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

     
        self.traits_canvas = tk.Canvas(self.traits_frame, height=250)  # Set a fixed height here
        self.traits_scrollbar = ttk.Scrollbar(self.traits_frame, orient="vertical", command=self.traits_canvas.yview)
        self.traits_scrollable_frame = ttk.Frame(self.traits_canvas)

        self.traits_canvas.create_window((0, 0), window=self.traits_scrollable_frame, anchor="nw")
        self.traits_scrollable_frame.bind("<Configure>", lambda e: self.traits_canvas.configure(scrollregion=self.traits_canvas.bbox("all")))

        self.traits_canvas.configure(yscrollcommand=self.traits_scrollbar.set)
        self.traits_canvas.grid(row=0, column=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.traits_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

       
        self.trait_options = {}
        available_propositions = set(fact['proposition'] for fact in knowledge_base['Facts'])

        for i, prop in enumerate(sorted(available_propositions)):
            label = ttk.Label(self.traits_scrollable_frame, text=prop)
            label.grid(row=i, column=0, sticky=tk.W, pady=2)

            var = tk.StringVar(value="Ignore")
            dropdown = ttk.Combobox(self.traits_scrollable_frame, textvariable=var, state="readonly", values=["Ignore", "Yes", "No"], width=15)  # Adjust width to 15 (pixels)
            dropdown.grid(row=i, column=1, sticky=tk.W, padx=5, pady=2)  # Add padding for better spacing
            self.trait_options[prop] = var

       
        self.algorithms_frame = ttk.LabelFrame(self.main_frame, text="Select Algorithm", padding="10")
        self.algorithms_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(20, 0))

        self.algorithm_var = tk.StringVar()
        self.forward_chaining_radio = ttk.Radiobutton(self.algorithms_frame, text="Forward Chaining", variable=self.algorithm_var, value="forward")
        self.backward_chaining_radio = ttk.Radiobutton(self.algorithms_frame, text="Backward Chaining", variable=self.algorithm_var, value="backward")
        self.forward_chaining_radio.grid(row=0, column=0, sticky=tk.W)
        self.backward_chaining_radio.grid(row=1, column=0, sticky=tk.W)

       
        self.results_frame = ttk.LabelFrame(self.main_frame, text="Identification Results", padding="10")
        self.results_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(20, 0))

        self.results_text = tk.Text(self.results_frame, width=60, height=10, wrap=tk.WORD)
        self.results_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.results_scrollbar = ttk.Scrollbar(self.results_frame, orient="vertical", command=self.results_text.yview)
        self.results_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.results_text.configure(yscrollcommand=self.results_scrollbar.set)

       
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.grid(row=3, column=0, columnspan=2, pady=(20, 0))

        self.identify_button = ttk.Button(self.button_frame, text="Identify Insect", command=self.identify_insect)
        self.clear_button = ttk.Button(self.button_frame, text="Clear Selections", command=self.clear_selections)
        self.identify_button.grid(row=0, column=0, padx=(0, 10))
        self.clear_button.grid(row=0, column=1, padx=(10, 0))

        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(1, weight=1)
        self.main_frame.rowconfigure(2, weight=1)

    def identify_insect(self):
        selected_traits = []
        for trait, var in self.trait_options.items():
            if var.get() == "Yes":
                selected_traits.append({"proposition": trait, "positive": True})
            elif var.get() == "No":
                selected_traits.append({"proposition": trait, "positive": False})

        if not selected_traits:
            self.results_text.delete("1.0", tk.END)
            self.results_text.insert(tk.END, "Error: Please select at least one trait.\n")
            return

        algorithm = self.algorithm_var.get()
        if not algorithm:
            self.results_text.delete("1.0", tk.END)
            self.results_text.insert(tk.END, "Error: Please select an algorithm.\n")
            return

        results = []
        for insect in set(rule["result"] for rule in knowledge_base["Rules"]):
            if algorithm == "forward" and forward_chaining(selected_traits, insect):
                results.append(next(info for info in insects_info if info["insect"] == insect))
            elif algorithm == "backward" and backward_chaining(selected_traits, insect):
                results.append(next(info for info in insects_info if info["insect"] == insect))

        self.display_results(results)

    def display_results(self, results):
        self.results_text.delete("1.0", tk.END)
        if results:
            for insect in results:
                self.results_text.insert(tk.END, f"Insect: {insect['insect']}\n")
                self.results_text.insert(tk.END, f"Description: {insect['description']}\n\n")
        else:
            self.results_text.insert(tk.END, "No matching insects found.\n")

    def clear_selections(self):
        for var in self.trait_options.values():
            var.set("Ignore")
        self.results_text.delete("1.0", tk.END)
        self.algorithm_var.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = InsectIdentificationGUI(root)
    root.mainloop()
