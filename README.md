<h1 align="center">AC Segmentation</h1>

<p align="center">
  Segments axons in volumetric light-microscopy OME-Zarr data with the Allen Institute ac_segmentation RSUNet model and outputs a labelled OME-Zarr volume.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.968"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.968-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-see_LICENSE-lightgrey.svg" alt="License"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Segments axons in volumetric light-microscopy OME-Zarr data with the Allen Institute ac_segmentation RSUNet model and outputs a labelled OME-Zarr volume.**

Runs the Allen Institute's segment_array.py with its bundled pretrained RSUNet checkpoint inside the gamorosino/ac-segmentation container, on CPU, using the first resolution level of the input OME-Zarr and an optional mask. Use it for automated axon segmentation of light-sheet or similar microscopy volumes.

| | |
|---|---|
| **Inputs** | `neuro/ome-zarr` · `neuro/ome-zarr` (optional) |
| **Outputs** | `neuro/ome-zarr` |
| **Container** | `gamorosino/ac-segmentation:latest` |
| **Resources** | 4 GB memory · 1 h walltime |
| **Run it** | [doi.org/10.25663/brainlife.app.968](https://doi.org/10.25663/brainlife.app.968) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `input` | `neuro/ome-zarr` | yes | Volumetric light-microscopy image (OME-Zarr); resolution level 0 is segmented. |
| `mask` | `neuro/ome-zarr` | no | Optional OME-Zarr mask restricting the segmentation. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `output` | `neuro/ome-zarr` | Segmented volume (uint8-labeled OME-Zarr) produced by the RSUNet model. |

<details>
<summary><b>Parameters</b> (2)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `dsfactor` | number | `1` | Mask downsample factor (segment_array.py --dsfactor). |
| `filter_max_intensity` | number | `30000` | Maximum intensity threshold used for contrast preprocessing before segmentation (segment_array.py --filter_max_intensity). |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.968](https://doi.org/10.25663/brainlife.app.968), choose `neuro/ome-zarr`, `neuro/ome-zarr` from your project, set the parameters and press **Execute**. The results are saved to your project as `neuro/ome-zarr`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `gamorosino/ac-segmentation:latest`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "input_path": "/path/to/input/input_path",
       "mask_path": "/path/to/mask/mask_path",
       "dsfactor": 1,
       "filter_max_intensity": 30000
   }
   ```

3. Run `./main`.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- AC Segmentation. brainlife.io App. [doi:10.25663/brainlife.app.968](https://doi.org/10.25663/brainlife.app.968)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

Wraps [AllenInstitute/ac_segmentation](https://github.com/AllenInstitute/ac_segmentation)
(`segment_array.py`, RSUNet model + bundled checkpoint), licensed GPLv3 by
the Allen Institute. That code is not redistributed here -- it runs inside
the pinned container image built from ac_segmentation's own Dockerfile.

- Gabriele Amorosino

## License

See [LICENSE](LICENSE).
