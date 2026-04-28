import codecs

content = []
with codecs.open('SKILL.md', 'r', 'utf-8') as f:
    for line in f:
        if line.startswith('## 📊'):
            break
        content.append(line)

new_content = "".join(content)
new_content += """## 📊 System Optimization Dashboard (LPO)

The following metrics power the "System Optimization Dashboard" radar chart on the portal's homepage. Update these values when you publish new strategic articles or achieve significant engineering milestones.

### 💼 仕事のスキル (Professional)
- **技術適応力**: 95
- **プロジェクト推進力**: 85
- **チーム貢献・SL力**: 75
- **課題解決・改善提案**: 90
- **ドメイン知識**: 85

### 💻 IT・テクニカルスキル (Technical)
- **IaC・構成管理**: 85
- **監視・可観測性**: 85
- **開発力(Frontend/Python)**: 85
- **生成AI・LLM活用**: 85
- **AIエージェント運用**: 80
"""

with codecs.open('SKILL.md', 'w', 'utf-8') as f:
    f.write(new_content)
