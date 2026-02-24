from __future__ import annotations

from dataclasses import dataclass, asdict

STYLE_MAP = {
    "cyberpunk": "赛博朋克霓虹、海岸城市夜景、高对比光影",
    "new_chinese": "新中式国潮、灯笼纹样、海浪与书法元素",
}


@dataclass
class PosterPack:
    title: str
    subtitle: str
    prompt_cn: str
    prompt_en: str
    cta: str
    sponsor_copy: str
    private_domain_copy: str


def generate_poster_pack(style: str, visual_focus: str, palette: str) -> dict:
    style_text = STYLE_MAP.get(style, STYLE_MAP["new_chinese"])

    title = "烟台元宵AI猜灯谜大会"
    subtitle = f"{visual_focus}主题 · {palette}色调"
    prompt_cn = (
        f"{style_text}，画面主体：{visual_focus}，节日氛围：元宵灯会，"
        f"加入烟台城市元素（海岸线、地标剪影、在地方言彩蛋），主色调：{palette}，4k海报质感"
    )
    prompt_en = (
        f"Yantai Lantern Festival poster, {style_text}, focus on {visual_focus}, "
        f"local landmarks silhouette, ocean vibe, festive lanterns, palette {palette}, 4k, ultra detailed"
    )
    cta = "评论区回复“猜谜”领完整答案，猜中可抽本地商家福利券。"
    sponsor_copy = "【商家联名】今晚猜中任意3题，到店出示截图立减8元。"
    private_domain_copy = "加V回复“元宵”领取谜底合集+同城活动地图。"

    return asdict(
        PosterPack(title, subtitle, prompt_cn, prompt_en, cta, sponsor_copy, private_domain_copy)
    )
