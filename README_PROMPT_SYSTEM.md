# Structured Prompt System for Local Business Website Copy

## Overview

This is a professional-grade prompt engineering system designed to generate high-quality website copy for local businesses. The system creates structured, detailed prompts that can be used with AI copywriting tools (ChatGPT, Claude, etc.) to produce the same caliber of content that web agencies charge thousands of dollars for.

## Features

- **Comprehensive Business Profiling**: Structured data collection for all essential business information
- **Multi-Section Coverage**: Generates prompts for all critical website sections
  - Hero Section (headline, subheadline, CTA)
  - About Us Section (brand story, credibility)
  - Services Section (benefit-focused descriptions)
  - Testimonial Guides (collection strategy)
  - Call-to-Action Sections (conversion optimization)
  - Meta Descriptions (SEO optimization)
- **Professional Quality**: Prompts designed with copywriting best practices
- **Benefit-Driven**: Focuses on customer benefits, not just features
- **Local SEO Optimized**: Built-in local relevance and location targeting
- **Flexible Output**: Export to JSON or print formatted prompts
- **Easy Integration**: Use with any AI tool of your choice

## Installation

No external dependencies required! This system uses only Python standard library.

```bash
# Clone the repository
git clone https://github.com/Mehalvinod/FUTURE_PE_01.git
cd FUTURE_PE_01

# Run the example
python prompt_system.py
```

## Quick Start

### 1. Using the Example

Run the included example to see the system in action:

```bash
python prompt_system.py
```

This will display all prompts for a sample plumbing business and export them to `website_copy_prompts.json`.

### 2. Creating Your Own Business Profile

```python
from prompt_system import BusinessProfile, WebsiteCopyGenerator

# Create your business profile
my_business = BusinessProfile(
    business_name="Green Leaf Landscaping",
    business_type="Landscaping & Lawn Care",
    location="Denver, CO",
    years_in_business=10,
    unique_value_proposition="Eco-friendly landscaping solutions that save water and reduce maintenance",
    target_audience="environmentally conscious homeowners in Denver",
    services=[
        "Landscape Design",
        "Lawn Maintenance",
        "Irrigation Systems",
        "Hardscaping"
    ],
    key_benefits=[
        "Water-efficient designs",
        "Native plant expertise",
        "Year-round maintenance plans",
        "Licensed and insured"
    ],
    customer_pain_points=[
        "High water bills",
        "Time-consuming yard work",
        "Plants that don't survive Colorado climate"
    ],
    brand_voice="friendly and knowledgeable, with environmental passion",
    call_to_action="Get Your Free Estimate",
    phone="(303) 555-0123",
    email="info@greenleafdenver.com"
)

# Generate prompts
generator = WebsiteCopyGenerator(my_business)
generator.print_prompts()  # Display all prompts
generator.export_prompts("my_business_prompts.json")  # Export to file
```

### 3. Generating Specific Sections

```python
# Generate just one section
hero_prompt = generator.generate_section_prompt("hero")
print(hero_prompt)

# Available sections: "hero", "about", "services", "testimonial", "cta", "meta"
```

## How to Use the Generated Prompts

1. **Generate Your Prompts**: Run the system with your business information
2. **Copy to AI Tool**: Take each prompt and paste it into ChatGPT, Claude, or your preferred AI
3. **Review the Output**: The AI will generate professional copy based on the structured prompt
4. **Customize**: Tweak the generated copy to match your exact needs
5. **Deploy**: Use the copy on your website

## Business Profile Fields

### Required Fields

- **business_name**: Your business name
- **business_type**: Type of business (e.g., "Restaurant", "Law Firm", "Plumbing")
- **location**: City and state (for local SEO)
- **years_in_business**: How long you've been operating
- **unique_value_proposition**: What makes you different/better
- **target_audience**: Who your ideal customers are
- **services**: List of services you offer

### Optional Fields

- **key_benefits**: Specific advantages you provide (default: empty list)
- **customer_pain_points**: Problems your customers face (default: empty list)
- **brand_voice**: Tone and style (default: "professional and friendly")
- **call_to_action**: Main CTA text (default: "Contact us today")
- **phone**: Contact phone number (default: None)
- **email**: Contact email (default: None)
- **website**: Website URL (default: None)

## What Makes These Prompts Effective

### 1. Context-Rich
Each prompt includes comprehensive business context, ensuring the AI generates relevant, specific copy rather than generic content.

### 2. Structured Requirements
Clear formatting and requirement guidelines ensure consistent, professional output every time.

### 3. Benefit-Focused
Prompts are designed to generate benefit-driven copy that converts visitors into customers.

### 4. Local SEO Integration
Built-in location awareness and local relevance for better search engine visibility.

### 5. Conversion Optimization
Every section is designed with conversion goals in mind, from attention-grabbing heroes to compelling CTAs.

## Example Output Structure

When you run the system, you'll get prompts for:

### Hero Section
- Attention-grabbing headline
- Supporting subheadline
- Clear call-to-action

### About Section
- Authentic brand story
- Trust-building elements
- Community connection

### Services Section
- Benefit-focused descriptions
- Feature highlights
- Customer value propositions

### Testimonial Guide
- Collection strategy
- Key themes to capture
- Questions to ask customers

### CTA Section
- Persuasive headlines
- Objection handling
- Multiple CTA options

### Meta Description
- SEO-optimized
- Local keywords
- Click-worthy copy

## Use Cases

This system is perfect for:

- **Web Agencies**: Generate copy prompts for client websites quickly
- **Freelance Copywriters**: Streamline your copywriting process
- **Business Owners**: Create professional website copy without hiring an agency
- **Marketing Teams**: Maintain consistency across multiple business locations
- **Web Developers**: Provide copywriting services alongside development

## Advanced Usage

### Batch Processing

Generate prompts for multiple businesses:

```python
businesses = [business1, business2, business3]
for business in businesses:
    generator = WebsiteCopyGenerator(business)
    filename = f"{business.business_name.replace(' ', '_')}_prompts.json"
    generator.export_prompts(filename)
```

### Custom Integration

```python
# Get all prompts as a dictionary
all_prompts = generator.generate_all_prompts()

# Process programmatically
for section, prompt in all_prompts.items():
    # Send to your AI API
    # Store in database
    # Process however you need
    pass
```

## Best Practices

1. **Be Specific**: The more detailed your BusinessProfile, the better the prompts
2. **Know Your Audience**: Clearly define your target audience for relevant copy
3. **Highlight Uniqueness**: Emphasize what makes the business special
4. **List Pain Points**: Understanding customer problems leads to better solutions-focused copy
5. **Test Variations**: Generate multiple versions and A/B test them

## Limitations

- This system generates **prompts**, not the final copy itself
- You'll need to use an AI tool (ChatGPT, Claude, etc.) to generate the actual copy
- Generated copy should be reviewed and customized for accuracy
- Some business-specific details may need manual adjustment

## Future Enhancements

Potential improvements to consider:

- Additional sections (FAQ, Team, Portfolio, Contact)
- Industry-specific templates
- Direct AI API integration
- Multi-language support
- A/B testing variations
- Tone analysis and optimization

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available for commercial and personal use.

## Support

For questions or support, please open an issue on the GitHub repository.

---

**Created for**: Web agencies, copywriters, and business owners who need professional website copy without the professional price tag.
