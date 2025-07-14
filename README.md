# EPUB to Markdown Converter

A Python script to convert EPUB files to Markdown format with proper nested headers and structured content.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Output Structure](#output-structure)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🔍 Overview

This tool converts EPUB files to Markdown format while preserving the document structure with nested headers. It's designed to handle multiple EPUB files in batch, making it easy to convert entire libraries of ebooks to a readable Markdown format.

The converter extracts content from EPUB files, processes the HTML structure, and outputs clean Markdown files with proper header hierarchy, making the content easily readable and navigable.

## ✨ Features

- **Batch Processing**: Convert multiple EPUB files at once
- **Nested Headers**: Maintains proper header hierarchy (# ## ### ####)
- **Metadata Preservation**: Extracts and includes book title and author information
- **Clean Output**: Removes scripts, styles, and other non-content elements
- **Filename Sanitization**: Converts filenames to safe, filesystem-compatible names
- **Error Handling**: Robust error handling with detailed reporting
- **Progress Tracking**: Shows conversion progress and results
- **Unicode Support**: Handles international characters properly

## 📋 Requirements

### System Requirements
- Python 3.7 or higher
- At least 1GB of free disk space (depending on EPUB collection size)
- Memory: 512MB RAM minimum (more for large EPUB files)

### Python Dependencies
- `ebooklib` - For reading EPUB files
- `beautifulsoup4` - For HTML parsing
- `html2text` - For HTML to Markdown conversion

## 🚀 Installation

### 1. Clone or Download
```bash
git clone <repository-url>
cd epub-to-markdown-converter
```

### 2. Install Dependencies
```bash
pip install ebooklib beautifulsoup4 html2text
```

Or using a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install ebooklib beautifulsoup4 html2text
```

### 3. Verify Installation
```bash
python3 epub_to_markdown.py --help
```

## 📖 Usage

### Basic Usage

1. **Prepare your EPUB files**: Place all EPUB files in the `epub` folder
2. **Run the converter**:
   ```bash
   python3 epub_to_markdown.py
   ```
3. **Check results**: Converted Markdown files will be in the `markdown_output` folder

### Directory Structure
```
project-root/
├── epub_to_markdown.py
├── epub/
│   ├── book1.epub
│   ├── book2.epub
│   └── book3.epub
├── markdown_output/
│   ├── book1.md
│   ├── book2.md
│   └── book3.md
└── README.md
```

### Command Line Examples

#### Convert all EPUB files in the epub folder:
```bash
python3 epub_to_markdown.py
```

#### Using virtual environment:
```bash
source venv/bin/activate
python3 epub_to_markdown.py
```

## 📁 Output Structure

Each converted Markdown file includes:

### 1. Book Metadata
```markdown
# Book Title

**Author:** Author Name

---
```

### 2. Table of Contents
Automatically generated with proper nesting:
```markdown
## Table of Contents

### Chapter 1: Introduction
#### 1.1 Getting Started
#### 1.2 Basic Concepts

### Chapter 2: Advanced Topics
#### 2.1 Complex Operations
#### 2.2 Best Practices
```

### 3. Content Structure
- **Main Title**: `# Book Title`
- **Parts/Sections**: `## Part 1: Introduction`
- **Chapters**: `### Chapter 1: Getting Started`
- **Subsections**: `#### 1.1 Basic Concepts`
- **Sub-subsections**: `##### 1.1.1 Fundamentals`

### 4. Preserved Elements
- **Text formatting**: Bold, italic, code blocks
- **Lists**: Ordered and unordered lists
- **Links**: External and internal links
- **Images**: Image references (with alt text)
- **Tables**: Markdown table format
- **Code blocks**: Syntax highlighting preserved

## ⚙️ Configuration

### Customizing Output

You can modify the script behavior by editing these variables in `epub_to_markdown.py`:

```python
# Input and output directories
epub_folder = "epub"          # Change source directory
output_folder = "markdown_output"  # Change output directory
```

### HTML2Text Settings

The script uses these `html2text` configurations:
```python
h.ignore_links = False        # Include links in output
h.ignore_images = False       # Include images in output
h.ignore_emphasis = False     # Include bold/italic formatting
h.body_width = 0             # Don't wrap lines
h.unicode_snob = True        # Handle Unicode properly
h.bypass_tables = False      # Convert tables to Markdown
```

### Filename Sanitization

The script automatically:
- Removes `.epub` extension
- Replaces special characters with underscores
- Removes multiple consecutive underscores
- Strips leading/trailing underscores
- Adds `.md` extension

## 🔧 Troubleshooting

### Common Issues

#### 1. "Module not found" error
```bash
ModuleNotFoundError: No module named 'ebooklib'
```
**Solution**: Install required dependencies
```bash
pip install ebooklib beautifulsoup4 html2text
```

#### 2. "Permission denied" error
**Solution**: Check file permissions
```bash
chmod +x epub_to_markdown.py
```

#### 3. Empty output files
**Possible causes**:
- Corrupted EPUB files
- DRM-protected EPUB files
- Unsupported EPUB format

**Solution**: Verify EPUB files are valid and DRM-free

#### 4. Memory errors with large files
**Solution**: Process files individually or increase available memory

#### 5. Unicode encoding issues
**Solution**: Ensure your system supports UTF-8 encoding

### Debug Mode

To enable verbose output, modify the script:
```python
# Add after imports
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Log Files

The script outputs conversion status to console. To save logs:
```bash
python3 epub_to_markdown.py > conversion.log 2>&1
```

## 🛠️ Advanced Usage

### Processing Single File

Modify the `main()` function to process a single file:
```python
def convert_single_file(epub_path, output_path):
    if convert_epub_to_markdown(epub_path, output_path):
        print(f"Successfully converted {epub_path}")
    else:
        print(f"Failed to convert {epub_path}")
```

### Custom Output Format

You can modify the `process_epub_content()` function to change output format:
```python
# Add custom header
content_parts.append(f"# {title[0][0]}\n\n")
content_parts.append(f"**Author:** {author[0][0]}\n\n")
content_parts.append(f"**Converted on:** {datetime.now().strftime('%Y-%m-%d')}\n\n")
```

### Batch Processing with Progress Bar

Install and use `tqdm` for progress tracking:
```bash
pip install tqdm
```

```python
from tqdm import tqdm

for epub_file in tqdm(epub_files, desc="Converting EPUBs"):
    # conversion code here
```

## 📝 Example Output

Here's what a converted file might look like:

```markdown
# Penetration Testing APIs

**Author:** John Doe

---

## Table of Contents

### Chapter 1: Introduction to API Security
#### Understanding APIs
#### Common Vulnerabilities

### Chapter 2: Authentication and Authorization
#### OAuth Implementation
#### JWT Tokens

## Chapter 1: Introduction to API Security

### Understanding APIs

APIs (Application Programming Interfaces) are...

#### REST APIs

REST APIs follow specific principles...

### Common Vulnerabilities

The most common API vulnerabilities include...

## Chapter 2: Authentication and Authorization

### OAuth Implementation

OAuth 2.0 is a widely used authorization framework...
```

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/new-feature`
3. **Make your changes**
4. **Add tests** if applicable
5. **Commit your changes**: `git commit -m "Add new feature"`
6. **Push to the branch**: `git push origin feature/new-feature`
7. **Create a Pull Request**

### Code Style
- Follow PEP 8 style guidelines
- Use meaningful variable names
- Add docstrings to functions
- Include error handling

### Testing
Before submitting, test with various EPUB files:
- Different publishers
- Various file sizes
- Different content types (text, images, tables)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [ebooklib](https://github.com/aerkalov/ebooklib) - EPUB reading library
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - HTML parsing
- [html2text](https://github.com/Alir3z4/html2text) - HTML to Markdown conversion

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#troubleshooting) section
2. Search existing [Issues](https://github.com/your-repo/issues)
3. Create a new issue with:
   - Python version
   - Operating system
   - Error messages
   - Sample EPUB file (if possible)

## 🔄 Changelog

### v1.0.0
- Initial release
- Basic EPUB to Markdown conversion
- Batch processing support
- Nested header structure
- Metadata extraction

---
