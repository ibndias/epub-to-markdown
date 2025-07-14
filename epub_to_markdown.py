#!/usr/bin/env python3
"""
Convert EPUB files to Markdown with nested headers
"""

import os
import re
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import html2text

def clean_filename(filename):
    """Clean filename for use as markdown filename"""
    # Remove .epub extension
    name = os.path.splitext(filename)[0]
    # Replace spaces and special characters with underscores
    name = re.sub(r'[^\w\-_\.]', '_', name)
    # Remove multiple underscores
    name = re.sub(r'_+', '_', name)
    # Remove leading/trailing underscores
    name = name.strip('_')
    return name + '.md'

def html_to_markdown(html_content):
    """Convert HTML content to Markdown with proper header nesting"""
    if not html_content:
        return ""
    
    # Create html2text instance
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.body_width = 0  # Don't wrap lines
    h.unicode_snob = True
    h.bypass_tables = False
    
    # Convert to markdown
    markdown_content = h.handle(html_content)
    
    return markdown_content

def process_epub_content(book):
    """Process EPUB content and extract text with proper structure"""
    content_parts = []
    
    # Get book metadata
    title = book.get_metadata('DC', 'title')
    author = book.get_metadata('DC', 'creator')
    
    if title:
        content_parts.append(f"# {title[0][0]}\n\n")
    
    if author:
        content_parts.append(f"**Author:** {author[0][0]}\n\n")
    
    content_parts.append("---\n\n")
    
    # Process each item in the book
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            # Get the content
            content = item.get_content().decode('utf-8')
            
            # Parse with BeautifulSoup
            soup = BeautifulSoup(content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Convert to markdown
            markdown = html_to_markdown(str(soup))
            
            if markdown.strip():
                content_parts.append(markdown)
                content_parts.append("\n\n")
    
    return "".join(content_parts)

def convert_epub_to_markdown(epub_path, output_path):
    """Convert a single EPUB file to Markdown"""
    try:
        print(f"Converting {epub_path}...")
        
        # Read the EPUB file
        book = epub.read_epub(epub_path)
        
        # Process the content
        markdown_content = process_epub_content(book)
        
        # Write to markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"Successfully converted to {output_path}")
        return True
        
    except Exception as e:
        print(f"Error converting {epub_path}: {str(e)}")
        return False

def main():
    """Main function to convert all EPUB files in the epub folder"""
    epub_folder = "epub"
    output_folder = "markdown_output"
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get all EPUB files
    epub_files = [f for f in os.listdir(epub_folder) if f.endswith('.epub')]
    
    print(f"Found {len(epub_files)} EPUB files to convert")
    
    successful_conversions = 0
    failed_conversions = 0
    
    for epub_file in epub_files:
        epub_path = os.path.join(epub_folder, epub_file)
        markdown_filename = clean_filename(epub_file)
        output_path = os.path.join(output_folder, markdown_filename)
        
        if convert_epub_to_markdown(epub_path, output_path):
            successful_conversions += 1
        else:
            failed_conversions += 1
    
    print(f"\nConversion complete!")
    print(f"Successfully converted: {successful_conversions}")
    print(f"Failed conversions: {failed_conversions}")

if __name__ == "__main__":
    main()
