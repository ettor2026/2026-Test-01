from services.poster_generator import generate_poster_pack
from services.riddle_generator import generate_riddles


def test_generate_riddles_count():
    items = generate_riddles(topic="mixed", count=5, tone="fun")
    assert len(items) == 5
    assert {"question", "answer", "explanation", "cta"}.issubset(items[0].keys())


def test_generate_riddles_invalid_count():
    try:
        generate_riddles(count=51)
        assert False, "should raise ValueError"
    except ValueError:
        assert True


def test_generate_poster_pack_fields():
    data = generate_poster_pack("cyberpunk", "所城里", "蓝紫霓虹")
    assert data["title"]
    assert "所城里" in data["subtitle"]
    assert "Yantai Lantern Festival" in data["prompt_en"]
