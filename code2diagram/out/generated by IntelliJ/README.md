# Directory Structure
.<br/>
├── Image<br/>
│   ├── hub-level<br/>
│   │   ├── (repo-name).svg<br/>
│   │   ├── (repo-name).svg<br/>
│   │   └── (repo-name).svg<br/>
│   └── repo-level<br/>
│       ├── (api-project-name).svg<br/>
│       ├── (api-project-name).svg<br/>
│       └── (api-project-name).svg<br/>
├── PUML<br/>
│   ├── hub-level<br/>
│   │   ├── (repo-name).puml<br/>
│   │   ├── (repo-name).puml<br/>
│   │   └── (repo-name).puml<br/>
│   └── repo-level<br/>
│       ├── (api-project-name).puml<br/>
│       ├── (api-project-name).puml<br/>
│       └── (api-project-name).puml<br/>
└── README.md<br/>
***
# Directory Description
## Image
This folder containing generated image from PUML files.

## PUML
This folder containing PUML files that will be converted into image files (.svg).

## hub-level/
This folder stores PUML for class diagram of each repositories. These PUML files containing classes from api/, core/, and web/.

## repo-level/
This folder stores PUML for class diagram inside each repositories.

***
# Notes
- welab-core-component has no .java file.