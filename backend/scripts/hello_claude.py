"""第一次调用 Claude API：让 LgClawd 打个招呼，并算出这次花了多少钱。

用法（在 backend/ 目录下，先在 .env 里填好 ANTHROPIC_API_KEY）：
    python scripts/hello_claude.py
"""

import anthropic
from dotenv import load_dotenv

MODEL = "claude-opus-5-5"
# 美元 / 百万 token。阶段 2 做成本统计时会挪到配置里。
PRICE_PER_MTOK = {"input": 4.00, "output": 20.00, "cache_read": 0.20, "cache_write": 5.00}

SYSTEM = "你是 LgClawd，一只住在工科生电脑里的像素 AI，说话简短、调皮。"


def main() -> None:
    load_dotenv()  # 把 .env 里的 ANTHROPIC_API_KEY 读进环境变量
    client = anthropic.Anthropic()

    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        output_config={"effort": "low"},  # 简单任务用低 effort，省 token
        system=SYSTEM,
        messages=[{"role": "user", "content": "用一句话跟抖音上的新观众打个招呼。"}],
    )

    if response.stop_reason == "refusal":
        print("模型拒绝了这次请求：", response.stop_details)
        return

    for block in response.content:
        if block.type == "text":
            print("Clawd：", block.text)

    usage = response.usage
    cache_read = usage.cache_read_input_tokens or 0
    cache_write = usage.cache_creation_input_tokens or 0
    cost = (
        usage.input_tokens * PRICE_PER_MTOK["input"]
        + usage.output_tokens * PRICE_PER_MTOK["output"]
        + cache_read * PRICE_PER_MTOK["cache_read"]
        + cache_write * PRICE_PER_MTOK["cache_write"]
    ) / 1_000_000
    print(f"\n输入 {usage.input_tokens} tokens，输出 {usage.output_tokens} tokens（含思考）")
    print(f"这次花了约 ${cost:.5f}")


if __name__ == "__main__":
    main()
