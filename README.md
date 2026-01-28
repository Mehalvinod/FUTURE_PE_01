# Structured Prompt System for Local Business Website Copy

A professional-grade prompt engineering system that generates high-quality website copy prompts for local businesses - delivering the same caliber of content that web agencies charge thousands of dollars for.

## 🎯 What This Does

This system creates structured, comprehensive prompts that can be used with AI tools (ChatGPT, Claude, etc.) to generate professional website copy for local businesses across all essential sections:

- **Hero Section**: Attention-grabbing headlines and CTAs
- **About Us**: Authentic brand storytelling
- **Services**: Benefit-focused service descriptions
- **Testimonials**: Strategic collection guides
- **Call-to-Action**: Conversion-optimized CTAs
- **Meta Descriptions**: SEO-optimized descriptions

## 🚀 Quick Start

### Run the Example
```bash
python prompt_system.py
```
This demonstrates the system with a sample plumbing business and exports prompts to `website_copy_prompts.json`.

### Interactive Mode
```bash
python interactive_cli.py
```
Guided wizard to create prompts for your own business.

### Programmatic Usage
```python
from prompt_system import BusinessProfile, WebsiteCopyGenerator

# Define your business
business = BusinessProfile(
    business_name="Your Business Name",
    business_type="Your Business Type",
    location="Your City, State",
    years_in_business=10,
    unique_value_proposition="What makes you unique",
    target_audience="Your ideal customers",
    services=["Service 1", "Service 2", "Service 3"]
)

# Generate prompts
generator = WebsiteCopyGenerator(business)
generator.print_prompts()  # Display all prompts
generator.export_prompts("prompts.json")  # Export to file
```

## 📚 Documentation

See [README_PROMPT_SYSTEM.md](README_PROMPT_SYSTEM.md) for complete documentation including:
- Detailed usage instructions
- Business profile field explanations
- Best practices
- Advanced usage examples

## 💡 Key Features

- ✅ **Zero Dependencies**: Pure Python, no external packages required
- ✅ **Professional Quality**: Built with copywriting best practices
- ✅ **Benefit-Driven**: Focuses on customer value, not just features
- ✅ **Local SEO**: Built-in location targeting
- ✅ **Flexible Output**: JSON export or formatted console output
- ✅ **Easy Integration**: Works with any AI tool

## 📦 What's Included

- `prompt_system.py` - Core prompt generation system
- `interactive_cli.py` - Interactive command-line interface
- `website_copy_prompts.json` - Example output
- `example_output.txt` - Sample console output
- `README_PROMPT_SYSTEM.md` - Complete documentation

## 🎓 How It Works

1. **Input**: Provide business information (name, services, location, etc.)
2. **Generate**: System creates structured prompts for each website section
3. **Copy to AI**: Paste prompts into ChatGPT, Claude, or your preferred AI
4. **Review**: Get professional copy that you can customize
5. **Deploy**: Use the copy on your website

## 🎯 Perfect For

- Web agencies building client websites
- Freelance copywriters streamlining their workflow
- Business owners creating their own website copy
- Marketing teams managing multiple locations
- Anyone needing professional website copy without agency prices

## 📄 License

Open source - free for commercial and personal use.
