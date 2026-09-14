# AC Segmentation

Automated axonal segmentation of volumetric light-microscopy Zarr data, using the Allen Institute's ac_segmentation RSUNet model (segment_array.py) with the model's bundled pretrained checkpoint.

## Inputs

- `input` (neuro/ome-zarr)
- `mask` (neuro/ome-zarr) -- optional

## Outputs

- `output` (neuro/ome-zarr) -- Segmented volume (uint8-labeled OME-Zarr) produced by the RSUNet model.

## Usage

Brainlife.io: run via `braise-app-run`/`braise-app-pipeline` (once registered
with `braise-app-create`), or the web UI.

Locally (outside brainlife): copy `config.json.example` to `config.json`,
fill in real file paths, then run `./main` from this directory. `main` pulls
its own container (`singularity exec docker://...`) -- no local install of
the underlying tool needed, only Singularity itself.

Entrypoint: `segment_array.py`, run from inside the pinned container
(`docker://gamorosino/ac-segmentation:latest`) -- not vendored into this repo,
see `segment_array.py` here for why.

Runs on CPU only: `segment_array.py`'s own `--gpu_device` argument is not
actually wired to the underlying pipeline as of the upstream code this app
pins, so it always executes on CPU regardless of what's passed. This app is
registered with `requires_gpu: false` to match.

## Credits

Wraps [AllenInstitute/ac_segmentation](https://github.com/AllenInstitute/ac_segmentation)
(`segment_array.py`, RSUNet model + bundled checkpoint), licensed GPLv3 by
the Allen Institute. That code is not redistributed here -- it runs inside
the pinned container image built from ac_segmentation's own Dockerfile.

## Authors

- Gabriele Amorosino <g.amorosino@gmail.com>

## License

This wrapper (`main`, `_brainlife_run.py`, config/docs) is MIT, see
`LICENSE`. The underlying tool it invokes (Allen Institute's
ac_segmentation) is GPLv3 -- see its own repository for terms.
