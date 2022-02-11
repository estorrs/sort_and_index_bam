arguments:
- position: 2
  valueFrom: output.sorted.bam
baseCommand:
- python
- /sort_and_index_bam/sort_and_index.py
class: CommandLineTool
cwlVersion: v1.0
id: sort_and_index_bam
inputs:
- id: input_bam
  inputBinding:
    position: 1
  type: File
- default: 0
  id: cpu
  inputBinding:
    position: 1
    prefix: --cpu
  type: int?
- default: /miniconda/envs/sort_and_index_bam/bin:$PATH
  id: environ_PATH
  type: string?
label: sort_and_index_bam
outputs:
- id: output_bam
  outputBinding:
    glob: output.sorted.bam
  type: File
- id: output_bam_index
  outputBinding:
    glob: output.sorted.bam.bai
  type: File
requirements:
- class: DockerRequirement
  dockerPull: estorrs/sort_and_index_bam:0.0.1
- class: ResourceRequirement
  coresMin: $(inputs.cpu)
  ramMin: 28000
- class: EnvVarRequirement
  envDef:
    PATH: $(inputs.environ_PATH)
