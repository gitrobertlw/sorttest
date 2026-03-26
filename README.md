# sorttest

write code in python for the following. Sort the packages using the following criteria: - A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm. - A package is **heavy** when its mass is greater or equal to 20 kg.

You must dispatch the packages in the following stacks:

- **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
- **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
- **REJECTED**: packages that are **both** heavy and bulky are rejected.

### Implementation

Implement the function **sort(width, height, length, mass)** (units are centimeters for the dimensions and kilogram for the mass). This function must return a string: the name of the stack where the package should go.

How it works:
First, it computes the volume.
Then it checks:
If the package is bulky
If the package is heavy
Finally, it applies the rules in order:
Both bulky and heavy → REJECTED
Either one → SPECIAL
Neither → STANDARD
