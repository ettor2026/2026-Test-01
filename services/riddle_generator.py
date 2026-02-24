from __future__ import annotations

import random
from dataclasses import dataclass, asdict
from typing import List

LOCAL_TOPICS = {
    "landmark": ["所城里", "养马岛", "孤独的鲸", "烟台山", "东炮台"],
    "specialty": ["烟台苹果", "大樱桃", "海肠捞饭", "鲅鱼水饺", "焖子"],
    "dialect": ["木乱", "真鲜亮", "嘎嘎好", "可得劲", "杠赛来"],
}

RIDDLE_PATTERNS = [
    "白天迎海风，夜里照渔火，老街故事装满肚（打一烟台元素）",
    "外表圆润甜，咬一口脆生生，秋天最红火（打一烟台元素）",
    "站在海边看它，孤零零却最上镜（打一烟台地标）",
    "名字带个岛，春夏最想跑，海水蓝得像滤镜（打一烟台元素）",
]

TONE_GUIDE = {
    "fun": "语气活泼，适合短视频评论区互动",
    "poetic": "语气偏诗意，适合海报文案",
}


@dataclass
class RiddleItem:
    question: str
    answer: str
    explanation: str
    cta: str


def _pick_pool(topic: str) -> List[str]:
    if topic == "mixed":
        return LOCAL_TOPICS["landmark"] + LOCAL_TOPICS["specialty"] + LOCAL_TOPICS["dialect"]
    return LOCAL_TOPICS.get(topic, LOCAL_TOPICS["landmark"])


def generate_riddles(topic: str = "mixed", count: int = 10, tone: str = "fun") -> List[dict]:
    if count < 1 or count > 50:
        raise ValueError("count must be between 1 and 50")

    pool = _pick_pool(topic)
    tone_text = TONE_GUIDE.get(tone, TONE_GUIDE["fun"])
    result: List[dict] = []

    for idx in range(count):
        answer = random.choice(pool)
        base_question = random.choice(RIDDLE_PATTERNS)
        question = f"{idx+1}. {base_question}"
        explanation = f"谜底是“{answer}”。本条参考风格：{tone_text}。"
        cta = "猜中请在评论区打“我在烟台”+答案，抽3人送汤圆红包。"
        result.append(asdict(RiddleItem(question, answer, explanation, cta)))

    return result
