**Basalt Mixing Equation**<br>
*Current Release*: v.0.0.1.1 
[![DOI](https://zenodo.org/badge/141566218.svg)](https://zenodo.org/badge/latestdoi/141566218)<br>
A short script that produces mixing data for the elemental and isotope mixing equation in Charles Langmuir's 1978 paper 
"A general mixing equation with applications to Icelandic basalts."

**The equation**<br>

*Ax + Bxy + Cy + D = 0*<br>

**The variables for ratio-ratio mixing**<br>
a<sub>1</sub>= y<sub>1</sub> ratio denominator, a<sub>2</sub>=y<sub>2</sub> ratio denominator<br>
b<sub>1</sub>= x<sub>1</sub> ratio denominator, b<sub>2</sub>=x<sub>2</sub> ratio denominator<br>

A  = a<sub>2</sub>*b<sub>1</sub>*y<sub>2</sub> - a<sub>1</sub>*b<sub>2</sub>*y<sub>1</sub><br>
B = a<sub>1</sub>*b<sub>2</sub> - a<sub>2</sub>*b<sub>1</sub><br>
C = a<sub>2</sub>*b<sub>1</sub>*x<sub>1</sub> - a<sub>1</sub>*b<sub>2</sub>*x<sub>2</sub><br>
D = a<sub>1</sub>*b<sub>2</sub>*x<sub>2</sub>*y<sub>1</sub> - a<sub>2</sub>*b<sub>1</sub>*x<sub>1</sub>*y<sub>2</sub><br>

**The variables for ratio-element mixing**<br>
This assumes the x-axis is the element and the y-axis is the ratio<br>
a<sub>1</sub>= y<sub>1</sub> ratio denominator, a<sub>2</sub>=y<sub>2</sub> ratio denominator<br>
b<sub>1</sub>, b<sub>2</sub> = 1, 1<br>
A  = a<sub>2</sub>*y<sub>2</sub> - a<sub>1</sub>*y<sub>1</sub><br>
B = a<sub>1</sub> - a<sub>2</sub><br>
C = a<sub>2</sub>*x<sub>1</sub> - a<sub>1</sub>*x<sub>2</sub><br>
D = a<sub>1</sub>*x<sub>2</sub>*y<sub>1</sub> - a<sub>2</sub>*x<sub>1</sub>*y<sub>2</sub><br>

**The variables for element mixing**<br>
a<sub>1</sub>, a<sub>2</sub>, b<sub>1</sub>. b<sub>2</sub> = 1, 1, 1, 1 <br>
A  = y<sub>2</sub> - y<sub>1</sub><br>
B = 0<br>
C = x<sub>1</sub> - x<sub>2</sub><br>
D = x<sub>2</sub>*y<sub>1</sub> - x<sub>1</sub>*y<sub>2</sub><br>

***References***<br>
Langmuir, C. H., Vocke, J. R., Hanson, G. N., & Hart, S. R. (1978). A General Mixing Equation with Applications to Icelandic Basalts. Earth and Planetary Science Letters , 37, 380-392.
