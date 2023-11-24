# text2sd

# Prerequisites
- Python 3.8.2 or above. Compatibility with older version is not guaranteed.

# Input File Criteria
- The input file must be in text file format (.txt)
- The required indentation for the input file is 4 spaces, not '\t' (tab).
- Each line that representing a caller method should ended with a colon (:).
- Method output (return) should be preceded with ">>"
- See input/sample for more infomartion.

# How To Use
- Locate your input files directory. i.e. "input-sample/"
> input-sample/
- Run "py text2sd.py \<input directory>"
```
py text2sd.py input-sample/
```
- The output will be in the "out" directory
```.
├── README.md
├── input-sample
├── lib
├── out
│   ├── img
│   └── puml
└── text2sd.py
```
