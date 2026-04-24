import os
import json

# The map of old HTML proxy paths to new ones (partial paths)
link_map = {
    "html/ai/1bit-llm-bonsai-8b.html": "html/ai/llm-research/1bit-llm-bonsai-8b.html",
    "html/ai/agent-orchestration.html": "html/ai/automation/agent-orchestration.html",
    "html/ai/ai-hallucination.html": "html/ai/llm-research/ai-hallucination.html",
    "html/ai/ai-research-prompts.html": "html/ai/llm-research/ai-research-prompts.html",
    "html/ai/ai-roi-finops-azure.html": "html/ai/automation/ai-roi-finops-azure.html",
    "html/ai/antigravity-n8n-pipeline.html": "html/ai/automation/antigravity-n8n-pipeline.html",
    "html/ai/bonsai-8b-mobile-guide.html": "html/ai/llm-research/bonsai-8b-mobile-guide.html",
    "html/ai/copilot-operation-deep-dive.html": "html/ai/automation/copilot-operation-deep-dive.html",
    "html/ai/enterprise-ai-ops-rag.html": "html/ai/llm-research/enterprise-ai-ops-rag.html",
    "html/ai/enterprise-copilot-architecture.html": "html/ai/automation/enterprise-copilot-architecture.html",
    "html/ai/enterprise-md-knowledge.html": "html/ai/llm-research/enterprise-md-knowledge.html",
    "html/ai/multi-tenant-rag-security.html": "html/ai/llm-research/multi-tenant-rag-security.html",
    "html/ai/openclaw-google-calendar-automation.html": "html/ai/automation/openclaw-google-calendar-automation.html",
    "html/ai/openclaw-search-skill.html": "html/ai/automation/openclaw-search-skill.html",
    "html/ai/operation-automation.html": "html/ai/automation/operation-automation.html",
    "html/ai/oss-automation-tools.html": "html/ai/automation/oss-automation-tools.html",
    "html/ai/rag-incremental-indexing.html": "html/ai/llm-research/rag-incremental-indexing.html",
    "html/ai/sier-ai-structural-shift.html": "html/ai/automation/sier-ai-structural-shift.html",
    "html/dev/ai-code-review-gitlab-devcontainer.html": "html/dev/ai-coding/ai-code-review-gitlab-devcontainer.html",
    "html/dev/ai-code-review-practical-prompts.html": "html/dev/ai-coding/ai-code-review-practical-prompts.html",
    "html/dev/ai-code-review-senior-guide.html": "html/dev/ai-coding/ai-code-review-senior-guide.html",
    "html/dev/ai-coding-tools-comparison-2026.html": "html/dev/ai-coding/ai-coding-tools-comparison-2026.html",
    "html/dev/altra-recommender-retrospective.html": "html/dev/modern-js/altra-recommender-retrospective.html",
    "html/dev/devcontainer-harbor-intro.html": "html/dev/container/devcontainer-harbor-intro.html",
    "html/dev/devcontainer-harbor-operations.html": "html/dev/container/devcontainer-harbor-operations.html",
    "html/dev/devcontainer-harbor-security.html": "html/dev/container/devcontainer-harbor-security.html",
    "html/dev/freeman-project-hp-retrospective.html": "html/dev/modern-js/freeman-project-hp-retrospective.html",
    "html/dev/openai-codex-guide-2026.html": "html/dev/ai-coding/openai-codex-guide-2026.html",
    "html/dev/openai-codex-pricing-security.html": "html/dev/ai-coding/openai-codex-pricing-security.html",
    "html/dev/redmine-api-usage.html": "html/dev/modern-js/redmine-api-usage.html",
    "html/dev/synthetic-pet-simulation.html": "html/dev/modern-js/synthetic-pet-simulation.html",
    "html/infra/aws-egress-cost-aurora-benefits.html": "html/infra/cloud/aws-egress-cost-aurora-benefits.html",
    "html/infra/aws-kms-cost-envelope-encryption.html": "html/infra/cloud/aws-kms-cost-envelope-encryption.html",
    "html/infra/aws-minimal-iac-patterns.html": "html/infra/cloud/aws-minimal-iac-patterns.html",
    "html/infra/aws-rds-backup-best-practices.html": "html/infra/backup/aws-rds-backup-best-practices.html",
    "html/infra/aws-rds-rubrik-complete-guide.html": "html/infra/backup/aws-rds-rubrik-complete-guide.html",
    "html/infra/aws-rds-tech-deep-dive.html": "html/infra/cloud/aws-rds-tech-deep-dive.html",
    "html/infra/aws-tech-analysis-2026.html": "html/infra/cloud/aws-tech-analysis-2026.html",
    "html/infra/ctk-auto-remediation.html": "html/infra/ops/ctk-auto-remediation.html",
    "html/infra/db-backup-transition-strategy.html": "html/infra/backup/db-backup-transition-strategy.html",
    "html/infra/enterprise-it-paradigm-shift-2026.html": "html/infra/cloud/enterprise-it-paradigm-shift-2026.html",
    "html/infra/next-gen-cmdb-strategy.html": "html/infra/ops/next-gen-cmdb-strategy.html",
    "html/infra/nowhere-ransomware-deep-analysis.html": "html/infra/ops/nowhere-ransomware-deep-analysis.html",
    "html/infra/obsidian-google-drive-sync.html": "html/infra/ops/obsidian-google-drive-sync.html",
    "html/infra/openai-codex-research.html": "html/infra/ops/openai-codex-research.html",
    "html/infra/openclaw-vps-network-troubleshoot.html": "html/infra/network/openclaw-vps-network-troubleshoot.html",
    "html/infra/oss-research-operation.html": "html/infra/ops/oss-research-operation.html",
    "html/infra/pagerduty-architecture.html": "html/infra/network/pagerduty-architecture.html",
    "html/infra/rds-onprem-backup-solutions.html": "html/infra/backup/rds-onprem-backup-solutions.html",
    "html/infra/redmine-basic-knowledge.html": "html/infra/ops/redmine-basic-knowledge.html",
    "html/infra/rubrik-api-502-timeout-guide.html": "html/infra/backup/rubrik-api-502-timeout-guide.html",
    "html/infra/rubrik-api-code-capture-guide.html": "html/infra/backup/rubrik-api-code-capture-guide.html",
    "html/infra/rubrik-api-code-capture.html": "html/infra/backup/rubrik-api-code-capture.html",
    "html/infra/rubrik-aws-rds-protection.html": "html/infra/backup/rubrik-aws-rds-protection.html",
    "html/infra/rubrik-backup-load-balancing.html": "html/infra/backup/rubrik-backup-load-balancing.html",
    "html/infra/rubrik-false-positive-analysis-guide.html": "html/infra/backup/rubrik-false-positive-analysis-guide.html",
    "html/infra/rubrik-graphql-xsoar-automation.html": "html/infra/backup/rubrik-graphql-xsoar-automation.html",
    "html/infra/rubrik-linux-lvm-flr-cause-guide.html": "html/infra/backup/rubrik-linux-lvm-flr-cause-guide.html",
    "html/infra/rubrik-linux-lvm-restore-guide.html": "html/infra/backup/rubrik-linux-lvm-restore-guide.html",
    "html/infra/rubrik-load-balancing-guide.html": "html/infra/backup/rubrik-load-balancing-guide.html",
    "html/infra/rubrik-log-export-guide.html": "html/infra/backup/rubrik-log-export-guide.html",
    "html/infra/rubrik-m365-alert-tuning.html": "html/infra/backup/rubrik-m365-alert-tuning.html",
    "html/infra/rubrik-max-object-counts-sizing.html": "html/infra/backup/rubrik-max-object-counts-sizing.html",
    "html/infra/rubrik-max-objects-limits.html": "html/infra/backup/rubrik-max-objects-limits.html",
    "html/infra/rubrik-ondemand-sla-retention.html": "html/infra/backup/rubrik-ondemand-sla-retention.html",
    "html/infra/rubrik-scaling-strategy-clusters-vs-nodes.html": "html/infra/backup/rubrik-scaling-strategy-clusters-vs-nodes.html",
    "html/infra/rubrik-scaling-strategy-nodes.html": "html/infra/backup/rubrik-scaling-strategy-nodes.html",
    "html/infra/rubrik-soar-automation-graphql.html": "html/infra/backup/rubrik-soar-automation-graphql.html",
    "html/infra/rubrik-tech-analysis-2026.html": "html/infra/backup/rubrik-tech-analysis-2026.html",
    "html/infra/rubrik-threat-log-extraction.html": "html/infra/backup/rubrik-threat-log-extraction.html",
    "html/infra/rubrik-threat-monitoring-fp.html": "html/infra/backup/rubrik-threat-monitoring-fp.html",
    "html/infra/rubrik-zero-trust-research.html": "html/infra/backup/rubrik-zero-trust-research.html",
    "html/infra/t-up-rubrik-api-integration-guide.html": "html/infra/ops/t-up-rubrik-api-integration-guide.html",
    "html/infra/vast-data-universal-storage-research.html": "html/infra/cloud/vast-data-universal-storage-research.html",
    "html/infra/vast-recovery-validation.html": "html/infra/cloud/vast-recovery-validation.html",
    "html/infra/webmethods-exponential-backoff-repeat.html": "html/infra/network/webmethods-exponential-backoff-repeat.html",
    "html/infra/webmethods-http-502-guide.html": "html/infra/network/webmethods-http-502-guide.html",
    "html/infra/webmethods-retry-storm-gateway.html": "html/infra/network/webmethods-retry-storm-gateway.html",
    "html/infra/webmethods-rubrik-502-master-guide.html": "html/infra/network/webmethods-rubrik-502-master-guide.html",
    "html/infra/win-110-scaling-fancyzones.html": "html/infra/ops/win-110-scaling-fancyzones.html",
    "html/infra/zombie-backup-asset-management-strategy.html": "html/infra/ops/zombie-backup-asset-management-strategy.html",
    "html/other/akasaka-meat-cospa-guide.html": "html/other/gourmet/akasaka-meat-cospa-guide.html",
    "html/other/akasaka-meat-gourmet-hub.html": "html/other/gourmet/akasaka-meat-gourmet-hub.html",
    "html/other/akasaka-meat-vip-guide.html": "html/other/gourmet/akasaka-meat-vip-guide.html",
    "html/other/esconfield-cospa-guide.html": "html/other/travel/esconfield-cospa-guide.html",
    "html/other/esconfield-vip-budget-guide.html": "html/other/travel/esconfield-vip-budget-guide.html",
    "html/other/kamakura-cospa-gourmet.html": "html/other/travel/kamakura-cospa-gourmet.html",
    "html/other/kamakura-zushi-lunch-hub.html": "html/other/travel/kamakura-zushi-lunch-hub.html",
    "html/other/kiss-principle-cognitive-limits.html": "html/other/tech-life/kiss-principle-cognitive-limits.html",
    "html/other/kutchan-local-foods.html": "html/other/travel/kutchan-local-foods.html",
    "html/other/niseko-1night2day-course.html": "html/other/travel/niseko-1night2day-course.html",
    "html/other/niseko-cospa-travel.html": "html/other/travel/niseko-cospa-travel.html",
    "html/other/niseko-onsen-gourmet-guide.html": "html/other/travel/niseko-onsen-gourmet-guide.html",
    "html/other/shinsenmarsh-trekking-guide.html": "html/other/travel/shinsenmarsh-trekking-guide.html",
    "html/other/stride-lab-niseko.html": "html/other/travel/stride-lab-niseko.html",
    "html/other/universe-spec-debug.html": "html/other/tech-life/universe-spec-debug.html",
    "html/other/yakitori-cospa-yokohama-kannai.html": "html/other/gourmet/yakitori-cospa-yokohama-kannai.html",
    "html/other/zushi-cospa-gourmet.html": "html/other/travel/zushi-cospa-gourmet.html",
    "html/other/zushi-yamanone-walk.html": "html/other/travel/zushi-yamanone-walk.html"
}

def update_links(root_dir):
    for root, dirs, files in os.walk(root_dir):
        if 'html' in root.split(os.sep): # Skip generated html directory
            continue
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                updated_content = content
                for old, new in link_map.items():
                    updated_content = updated_content.replace(old, new)
                
                if updated_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    print(f"Updated links in: {file_path}")

if __name__ == "__main__":
    update_links('.')
