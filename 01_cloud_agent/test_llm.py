import sys
sys.stdout.reconfigure(encoding='utf-8')
from openai import OpenAI

client = OpenAI(
    api_key="sk-f2a91f7bbcc24879a582e99ec8ddbc6f.sk70jP5a6SJ8aBwQ",
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

resp = client.chat.completions.create(
    model="glm-4-flash",
    messages=[{"role":"user","content":"你好，请简单介绍AI Agent"}]
)
print(resp.choices[0].message.content)
