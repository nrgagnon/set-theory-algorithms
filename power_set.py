from sys import argv

class MathSet:
    def __init__(self, elements):
        self.elements = []
        for element in elements:
            if element not in self.elements:
                self.elements.append(element)

    def insert(self, element):
        self.elements.append(element)

    def get_elements(self):
        return self.elements

    def cardinality(self):
        return len(self.elements)

    def power_set(self):
        if len(self.elements) == 0:
            return MathSet([[]]) 
        acc = [MathSet([]), MathSet([self.elements[0]])]
        if len(self.elements) > 1:
            for j in range(1, len(self.elements)):
                for k in range(0, 2 ** j):
                    if k == 0:
                        acc.append(MathSet([self.elements[j]]))
                    else:
                        new_set = acc[k]
                        new_set.insert(self.elements[j])
                        acc.append(new_set)
        return MathSet(acc)

def formatted(mSet):
    elements = mSet.get_elements()
    if len(elements) == 0:
        return "{}"
    string = "{"
    for element in elements:
        if isinstance(element, MathSet):
            string += formatted(element) + (", " if element != elements[-1] else "}")
        else:
            string += str(element) + (", " if element != elements[-1] else "}")
    return string

M = MathSet([1, 3, 7, 9])
M.insert(6)
print(formatted(M.power_set()))
