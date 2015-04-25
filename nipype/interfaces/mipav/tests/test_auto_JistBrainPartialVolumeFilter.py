# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.mipav.developer import JistBrainPartialVolumeFilter

def test_JistBrainPartialVolumeFilter_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inInput=dict(argstr='--inInput %s',
    ),
    inPV=dict(argstr='--inPV %s',
    ),
    inoutput=dict(argstr='--inoutput %s',
    ),
    null=dict(argstr='--null %s',
    ),
    outPartial=dict(argstr='--outPartial %s',
    hash_files=False,
    ),
    terminal_output=dict(nohash=True,
    ),
    xDefaultMem=dict(argstr='-xDefaultMem %d',
    ),
    xMaxProcess=dict(argstr='-xMaxProcess %d',
    usedefault=True,
    ),
    xPrefExt=dict(argstr='--xPrefExt %s',
    ),
    )
    inputs = JistBrainPartialVolumeFilter.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_JistBrainPartialVolumeFilter_outputs():
    output_map = dict(outPartial=dict(),
    )
    outputs = JistBrainPartialVolumeFilter.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
