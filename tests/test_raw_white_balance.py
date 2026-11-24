import pytest
import imaging.raw_white_balance as mod

CASES = [
    ("scene_partition", (1,)),
    ("highlight_clip", (1,)),
    ("luma_weight", (1,)),
    ("gain_step_limit", (1,)),
    ("camera_matrix", (1,)),
    ("determinism", (1,)),
    ("temporal_smooth", (1,)),
    ("validation", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("gray_world", (1,)),
    ("metrics", (1,)),
    ("estimate", (1,)),
    ("apply_gain", (1,)),
    ("tint", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
