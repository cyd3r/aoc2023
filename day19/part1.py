from pathlib import Path
import re

workflows = {}
all_xmas = []
with open(Path(__file__).parent / "input.txt") as f:
    for line in f.readlines():
        if not line.strip():
            continue
        if line.startswith("{"):
            values = line.strip()[1:-1].split(",")
            pairs = [v.split("=") for v in values]
            xmas = {k: int(v) for k, v in pairs}
            all_xmas.append(xmas)
        else:
            workflow, rest = line.strip().split("{")
            rest = rest[:-1]
            instructions = []
            for instr in rest.split(","):
                if ":" in instr:
                    if "<" in instr:
                        cmp = "<"
                    elif ">" in instr:
                        cmp = ">"
                    else:
                        raise RuntimeError()
                    check, to = instr.split(":")
                    categ, value = check.split(cmp)
                    instructions.append(
                        {"cmp": cmp, "value": int(value), "categ": categ, "to": to}
                    )
                else:
                    instructions.append({"to": instr})

            workflows[workflow] = instructions

print(all_xmas)
print(workflows)


def eval_workflow(xmas, w='in'):
    while w not in ("A", "R"):
        flow = workflows[w]
        for instr in flow:
            if "cmp" in instr:
                if instr["cmp"] == "<":
                    if xmas[instr["categ"]] < instr["value"]:
                        w = instr["to"]
                        break
                elif instr["cmp"] == ">":
                    if xmas[instr["categ"]] > instr["value"]:
                        w = instr["to"]
                        break
            else:
                w = instr["to"]
                break
    return w

output = 0
for xmas in all_xmas:
    if eval_workflow(xmas) == 'A':
        output += sum(xmas.values())
print(output)