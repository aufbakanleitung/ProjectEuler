class Herman:
    def __init__(self, *values):
        self.values = values

    def __repr__(self):
        if len(self.values) == 0:
            return "This is an object oriented Herman 🤘"
        elif len(self.values) == 1:
            return f"Herman is {self.values[0]}"
        elif len(self.values) == 2:
            return f"Herman is {self.values[0]}, because {self.values[1]}"
        elif len(self.values) == 3:
            return f"Herman is {self.values[0]}, because {self.values[1]} and this {self.values[2]}."
        else:
            return "Herman is confused 🥺"


h0 = Herman()  # Initiate a Herman
h3 = Herman("proud", "Dana is using state of the art tech", "is important if you want to stay relevant")
h_sad = Herman("also sad", "Dana is on Windows", "means she can't have the same beautiful terminal experience")

print(h0)
print(h3)
print("However ☝")
print(h_sad)
