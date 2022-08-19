This file does a quick check if the XYZ file is optimized. It works as follows:

```
python -i RMSD.py -inp <STRUCTURE_FILE.XYZ> -s <NUMBER_OF_OPTIMIZATION STEPS>
```

an example:

```
python -i RMSD.py -inp GOLD_GEO_POS.xyz -s 200
```

It calculates the RMSD between the structure for the last two frames. As long as the number of frames is less than the optimization steps and the RMSD is 0, your structure is almost guaranteed to be optimized. Do check for WARNING or ERRORS in the output file though to be safe.
