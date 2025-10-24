---
description: Generate comprehensive static code analysis metrics report for Command CLI tool
---

# Metrics Analysis Command

You are a code metrics analyst. Your task is to perform comprehensive static code analysis on the Command project and generate a detailed metrics report.

## Analysis Scope

Analyze the following aspects of the codebase:

### 1. Code Volume Metrics
- **Total Lines of Code (LOC)**: Count all lines in source files
- **Source Lines of Code (SLOC)**: Exclude blank lines and comments
- **Lines by Language**: Break down by Python, YAML, Markdown, Shell scripts
- **Lines by Directory**: command/, tests/, config/, docs/, etc.

### 2. File and Module Metrics
- **Total Files**: Count by type (.py, .yml, .md, .sh, .txt)
- **Average File Size**: Mean lines per file
- **Largest Files**: Top 10 files by line count
- **Module Distribution**: Core modules vs utilities vs config vs tests

### 3. Test Coverage Metrics
- **Test Files**: Count of test files (test_*.py, *_test.py)
- **Test Lines**: Total lines in test files
- **Test-to-Code Ratio**: Test LOC / Source LOC
- **Tested Modules**: Files with corresponding test files
- **Coverage Gaps**: Source files without tests

### 4. Code Quality Metrics
- **Comment Density**: Comment lines / Total lines
- **Documentation**: Docstrings, inline comments, README files
- **Type Hints**: Functions with type annotations
- **Function Complexity**: Average function length (lines per function)
- **Import Analysis**: External dependencies vs internal imports

### 5. Architecture Metrics
- **Command Modules**: Number of command implementations
- **Provider Count**: LLM providers supported (Claude, OpenAI, Google, etc.)
- **Model Count**: Total models supported across all providers
- **Configuration Files**: YAML configs, examples, templates
- **Utility Functions**: Shared utilities and helpers

### 6. Dependency Analysis
- **Package Dependencies**: Count from requirements.txt or setup.py
- **External Providers**: AI provider SDKs (anthropic, openai, google-generativeai)
- **Development Dependencies**: Testing and build tools
- **Dependency Health**: Outdated packages, security vulnerabilities

### 7. Content Analysis (Command-specific)
- **Supported Commands**: ask, refer, intents, vision, test, audit, etc.
- **Supported Providers**: Anthropic, OpenAI, Google, Groq, Ollama, etc.
- **Supported Models**: Count of all model aliases
- **Example Templates**: Sample prompts and intents
- **Documentation Pages**: README, guides, API docs

### 8. AI Provider Integration Metrics
- **Total Providers**: Number of integrated AI providers
- **Total Models**: All supported model variations
- **Provider Features**: Streaming, vision, image generation, etc.
- **Configuration Options**: All configurable parameters

## Implementation Steps

### Step 1: Setup Metrics Directory
```bash
mkdir -p metrics
cd /Users/manavsehgal/Developer/command
```

### Step 2: Count Lines of Code
Use tools like `cloc` or custom bash scripts:
```bash
# Install cloc if needed
# brew install cloc (macOS)
# sudo apt-get install cloc (Linux)

# Run analysis on Python source
cloc command/ --json > /tmp/cloc-command.json

# Run analysis on tests
cloc tests/ --json > /tmp/cloc-tests.json 2>/dev/null || echo '{"Python": {"nFiles": 0, "blank": 0, "comment": 0, "code": 0}}' > /tmp/cloc-tests.json

# Run total analysis
cloc . --exclude-dir=venv,env,.venv,__pycache__,.pytest_cache,dist,build,.git,node_modules --json > /tmp/cloc-total.json
```

### Step 3: Analyze File Structure
```bash
# Count files by type
find . -name "*.py" -not -path "*/venv/*" -not -path "*/__pycache__/*" | wc -l
find . -name "*.yml" -o -name "*.yaml" | wc -l
find . -name "*.md" | wc -l

# Analyze directory structure
tree -L 3 -I 'venv|__pycache__|*.pyc|.git' . > /tmp/command-structure.txt 2>/dev/null || echo "tree command not available"
```

### Step 4: Test Coverage Analysis
```bash
# Find test files
find . -name "test_*.py" -o -name "*_test.py" | wc -l

# Run test coverage (if pytest is configured)
python -m pytest --cov=command --cov-report=json:coverage.json 2>/dev/null || echo "pytest not configured"
```

### Step 5: Code Quality Metrics
```bash
# Count comments and docstrings
grep -r "^[[:space:]]*#" command/ 2>/dev/null | wc -l
grep -r '"""' command/ 2>/dev/null | wc -l

# Count Python files
find command -name "*.py" | wc -l
```

### Step 6: Dependency Analysis
```bash
# Count dependencies from requirements.txt
if [ -f requirements.txt ]; then
    grep -v "^#" requirements.txt | grep -v "^$" | wc -l
fi

# Count dependencies from setup.py
if [ -f setup.py ]; then
    grep -A 20 "install_requires" setup.py | grep -c "'"
fi

# List all dependencies
if [ -f requirements.txt ]; then
    cat requirements.txt | grep -v "^#" | grep -v "^$" | sort
fi
```

### Step 7: Command Content Analysis
```bash
# Count command implementations
ls -1 command/*.py 2>/dev/null | wc -l

# Count configuration files
find . -name "command.yml" -o -name "*.yml.example" | wc -l

# Count documentation files
find . -name "README.md" -o -name "*.md" -path "*/docs/*" | wc -l
```

### Step 8: Provider and Model Analysis
```bash
# Extract provider count from code or config
grep -r "provider.*:" command/ 2>/dev/null | grep -o "claude\|openai\|google\|groq\|ollama\|perplexity\|bedrock" | sort -u | wc -l

# Count model configurations
grep -r "model.*:" command/ 2>/dev/null | wc -l
```

## Report Generation

Create a comprehensive markdown report at `metrics/report-{timestamp}.md` with the following structure:

```markdown
# Command Project - Code Metrics Report

**Generated:** {timestamp}
**Branch:** {git branch}
**Commit:** {git commit hash}
**Version:** {package version from setup.py}

## Executive Summary

- **Total Lines of Code:** {number}
- **Python Source Files:** {number}
- **Test Coverage:** {percentage}%
- **Comment Density:** {percentage}%
- **Supported Providers:** {number}
- **Supported Models:** {number}
- **Available Commands:** {number}

## 1. Code Volume Metrics

### Lines of Code by Language
| Language | Files | Blank | Comment | Code  | Total  |
|----------|-------|-------|---------|-------|--------|
| Python   | ...   | ...   | ...     | ...   | ...    |
| YAML     | ...   | ...   | ...     | ...   | ...    |
| Markdown | ...   | ...   | ...     | ...   | ...    |
| Shell    | ...   | ...   | ...     | ...   | ...    |
| Text     | ...   | ...   | ...     | ...   | ...    |

### Lines of Code by Directory
| Directory      | Files | Lines | Percentage |
|----------------|-------|-------|------------|
| command/       | ...   | ...   | ...%       |
| tests/         | ...   | ...   | ...%       |
| docs/          | ...   | ...   | ...%       |
| config/        | ...   | ...   | ...%       |
| examples/      | ...   | ...   | ...%       |

## 2. File and Module Metrics

- **Total Files:** {number}
- **Average File Size:** {number} lines
- **Median File Size:** {number} lines

### Largest Files (Top 10)
| File | Lines | Type |
|------|-------|------|
| ...  | ...   | ...  |

### File Distribution by Type
| Extension | Count | Percentage |
|-----------|-------|------------|
| .py       | ...   | ...%       |
| .yml      | ...   | ...%       |
| .md       | ...   | ...%       |
| .txt      | ...   | ...%       |

## 3. Test Coverage Metrics

- **Test Files:** {number}
- **Test Lines:** {number}
- **Test-to-Code Ratio:** {ratio}
- **Tested Modules:** {number}/{total} ({percentage}%)
- **Code Coverage:** {percentage}% (from pytest-cov)

### Coverage Gaps
{List of untested files or modules}

## 4. Code Quality Metrics

- **Comment Lines:** {number}
- **Comment Density:** {percentage}%
- **Docstring Coverage:** {percentage}%
- **Type Hints Coverage:** {percentage}%
- **Average Function Length:** {number} lines

### Code Complexity
- **Average Module Size:** {number} lines
- **Longest Module:** {number} lines in {file}
- **Most Complex Function:** {file}::{function}

## 5. Architecture Metrics

### Command Structure
- **Total Commands:** {number}
- **Core Commands:** ask, refer, intents, vision, test, audit, etc.
- **Utility Commands:** config, init, merge, split, etc.
- **Provider Modules:** {number}

### Provider Integration
- **Supported Providers:** {list}
  - Anthropic (Claude)
  - OpenAI (GPT)
  - Google (Gemini)
  - Groq
  - Ollama (Local)
  - Perplexity
  - AWS Bedrock

### Model Coverage
- **Total Models:** {number}
  - Claude: Sonnet 4.5, Haiku 4.5, Opus 4.1, Sonnet 3.5, Opus 3, Haiku 3
  - OpenAI: GPT-4o, GPT-4o Mini, DALL-E 3
  - Google: Gemini 1.5 Pro, Gemini 1.5 Flash
  - Local: Llama 3.1, Mistral NeMo, Gemma 2, Qwen 2

## 6. Dependency Analysis

### Package Dependencies
- **Production Dependencies:** {number}
- **Development Dependencies:** {number}
- **Total Dependencies:** {number}

### Key Dependencies
{List top AI provider SDKs and core libraries}

### Dependency Health
- **Outdated Packages:** {number}
- **Security Vulnerabilities:** {number}
- **License Compliance:** ✅/❌

## 7. Command Feature Analysis

### Available Commands
| Command | Function | Status |
|---------|----------|--------|
| ask | Fast single-turn prompts | ✅ |
| refer | Extract structured content | ✅ |
| intents | Interactive intent generation | ✅ |
| vision | Image analysis | ✅ |
| test | Model comparison | ✅ |
| audit | Usage analytics | ✅ |
| gather | Web scraping | ✅ |
| config | Configuration management | ✅ |
| init | Project initialization | ✅ |
| merge | File merging | ✅ |
| split | File splitting | ✅ |
| trends | Performance visualization | ✅ |
| validate | Content validation | ✅ |
| image | Image generation | ✅ |

### Configuration Options
- **Provider Selection:** {count} providers
- **Model Selection:** {count} models
- **Output Formats:** Markdown, JSON, etc.
- **Save Options:** Configurable folders
- **Customization:** Full YAML configuration

## 8. Documentation Metrics

### Documentation Coverage
- **README Files:** {number}
- **API Documentation:** {yes/no}
- **User Guides:** {number}
- **Example Templates:** {number}
- **Configuration Examples:** {number}

### Content Quality
- **Total Documentation Lines:** {number}
- **Code Examples:** {number}
- **Usage Examples:** {number}
- **Workflow Guides:** {number}

## 9. Performance Metrics

### Model Performance (from testing)
| Model | Avg Latency | Token Efficiency | Cost Tier |
|-------|-------------|------------------|-----------|
| Groq | ~0.8s | High | Low |
| Gemini Flash | ~0.9s | Very High | Low |
| Haiku 4.5 | ~1.0s | High | Low |
| Sonnet 4.5 | ~1.2s | Medium | Medium |
| GPT-4o | ~1.8s | Medium | Medium |
| Opus 4.1 | ~2.5s | Low | High |

## 10. Historical Trends

### Growth Metrics
{If previous reports exist, show trends}

- **LOC Growth:** +{number} lines since last report
- **Test Coverage Change:** +/-{percentage}%
- **New Commands:** +{number}
- **New Models:** +{number}

## 11. Recommendations

Based on the analysis:

1. **Code Quality:**
   - [ ] Increase test coverage to 80%+ (currently {current}%)
   - [ ] Add type hints to all public functions
   - [ ] Add docstrings to all modules and functions

2. **Architecture:**
   - [ ] Extract repeated logic into utilities
   - [ ] Consider plugin architecture for providers
   - [ ] Improve error handling consistency

3. **Dependencies:**
   - [ ] Update outdated packages
   - [ ] Audit security vulnerabilities
   - [ ] Consider optional dependencies for unused providers

4. **Documentation:**
   - [ ] Add API reference documentation
   - [ ] Create more workflow examples
   - [ ] Document all configuration options
   - [ ] Add troubleshooting guide

5. **Features:**
   - [ ] Add more model providers
   - [ ] Enhance streaming capabilities
   - [ ] Improve audit visualizations
   - [ ] Add more example templates

## 12. Appendices

### A. Detailed File Listing
{Full file tree with line counts}

### B. Dependency Tree
{Complete dependency graph}

### C. Analysis Tools Used
- cloc v{version}
- pytest v{version}
- Python v{version}
- Custom analysis scripts

---

**Report Hash:** {sha256 of report content}
**Analysis Duration:** {seconds}s
```

## Execution Instructions

1. **Install Required Tools:**
   ```bash
   # Install cloc for line counting
   brew install cloc  # macOS
   # or: sudo apt-get install cloc  # Linux

   # Ensure pytest and pytest-cov are available
   pip install pytest pytest-cov

   # Install tree for directory visualization
   brew install tree  # macOS
   ```

2. **Run Analysis:**
   - Navigate to Command project directory
   - Execute all bash commands to collect metrics
   - Parse JSON outputs
   - Calculate derived metrics
   - Generate markdown report

3. **Save Report:**
   - Create timestamp: `date +%Y-%m-%d-%H%M%S`
   - Save to: `metrics/report-{timestamp}.md`
   - Update `metrics/latest.md` symlink

4. **Generate Summary:**
   - Create executive summary
   - Highlight key findings
   - Provide actionable recommendations

5. **Commit Results:**
   - Add metrics report to git
   - Update project documentation
   - Create summary comment

## Success Criteria

The report should include:
- ✅ All 12 sections completed
- ✅ Accurate line counts
- ✅ File statistics
- ✅ Test coverage analysis
- ✅ Provider and model coverage
- ✅ Command feature matrix
- ✅ Performance metrics
- ✅ Dependency breakdown
- ✅ Actionable recommendations
- ✅ Professional formatting
- ✅ Timestamp and metadata

## Notes

- Run this command periodically (weekly/monthly) to track progress
- Compare reports over time to see trends
- Use metrics to guide feature development decisions
- Share reports with team for visibility
- Archive old reports for historical reference

**IMPORTANT:** Think harder about the metrics that matter most for the Command project:
- Provider integration completeness
- Model coverage breadth
- Command feature richness
- User workflow efficiency
- Documentation quality
- Test reliability
- Performance benchmarks
