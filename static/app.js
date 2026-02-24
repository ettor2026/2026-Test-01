const riddleOutput = document.getElementById('riddleOutput');
const posterOutput = document.getElementById('posterOutput');

document.getElementById('genRiddles').addEventListener('click', async () => {
  const payload = {
    topic: document.getElementById('topic').value,
    count: Number(document.getElementById('count').value),
    tone: document.getElementById('tone').value,
  };

  const res = await fetch('/api/riddles', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(payload)
  });

  const data = await res.json();
  if (!res.ok) {
    riddleOutput.textContent = `生成失败: ${data.error}`;
    return;
  }

  riddleOutput.textContent = data.items
    .map(item => `${item.question}\n谜底：${item.answer}\n解释：${item.explanation}\n引导：${item.cta}`)
    .join('\n\n');
});

document.getElementById('genPoster').addEventListener('click', async () => {
  const payload = {
    style: document.getElementById('style').value,
    visual_focus: document.getElementById('visual').value,
    palette: document.getElementById('palette').value,
  };

  const res = await fetch('/api/poster', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(payload)
  });

  const data = await res.json();
  posterOutput.textContent = [
    `标题：${data.title}`,
    `副标题：${data.subtitle}`,
    `中文提示词：${data.prompt_cn}`,
    `English Prompt: ${data.prompt_en}`,
    `互动CTA：${data.cta}`,
    `商家赞助文案：${data.sponsor_copy}`,
    `私域引导文案：${data.private_domain_copy}`,
  ].join('\n\n');
});
