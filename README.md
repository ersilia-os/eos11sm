# Ressemblance to a curated list of known antibiotics

A curated list of about 600 known antibiotics from AntibioticDB and the Collins lab (MIT) is used as a reference to identify compounds that ressemble known antibiotics. The tool can be used, for example, to remove unattractive compounds in virtual screening. The ressemblance score is computed using a logistic regression taking into account Tanimoto similarity over multiple molecular fingerprints.

This model was incorporated on 2025-11-24.Last packaged on 2025-11-25.

## Information
### Identifiers
- **Ersilia Identifier:** `eos11sm`
- **Slug:** `known-antibiotic-ressemblance`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Antimicrobial resistance`
- **Target Organism:** `Any`
- **Tags:** `Antimicrobial activity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** A score of 1 indicates high ressemblance to known antibiotics, while a score of 0 indicates low ressemblance.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| abx_score | float | high | Score indicating the likelihood of being an antibiotic compound |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos11sm](https://hub.docker.com/r/ersiliaos/eos11sm)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos11sm.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos11sm.zip)

### Resource Consumption
- **Model Size (Mb):** `6`
- **Environment Size (Mb):** `778`
- **Image Size (Mb):** `728.06`

**Computational Performance (seconds):**
- 10 inputs: `28.55`
- 100 inputs: `18.63`
- 10000 inputs: `104.87`

### References
- **Source Code**: [https://github.com/ersilia-os/ersilia](https://github.com/ersilia-os/ersilia)
- **Publication**: [https://antibioticdb.com](https://antibioticdb.com)
- **Publication Type:** `Other`
- **Publication Year:** `2025`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-or-later](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos11sm
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos11sm
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
