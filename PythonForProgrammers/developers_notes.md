# Developer's Notes - Python for Programmers

Brett Deaton - Dec 2021

To convert these jupyter notebooks to Reveal.js slide shows:

* open the Property Inspector (gears icon on the right side of JupyterLab interface)
* choose "Slide Type" for each cell block
* and export to html using File > "Save and Export Notebook As..." > Reveal.js Slides

Alternatively, I think you may have more control with some sort of `nbconvert` configuration file (see [docs](https://nbconvert.readthedocs.io/en/latest/config_options.html)), then rendering the slides from the command line

```
> python3 -m nbconvert --to slides --post serve notes-intro_to_python.ipynb
```