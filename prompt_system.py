"""
Structured Prompt System for Local Business Website Copy Generation

This module provides a comprehensive prompt engineering system that generates
high-quality website copy for local businesses, similar to what web agencies
provide to their clients.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field
import json


@dataclass
class BusinessProfile:
    """
    Data structure to hold essential business information for copy generation.
    """
    business_name: str
    business_type: str
    location: str
    years_in_business: int
    unique_value_proposition: str
    target_audience: str
    services: List[str]
    key_benefits: List[str] = field(default_factory=list)
    customer_pain_points: List[str] = field(default_factory=list)
    brand_voice: str = "professional and friendly"
    call_to_action: str = "Contact us today"
    phone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None


class PromptTemplates:
    """
    Collection of structured prompt templates for different website sections.
    Each template is designed to generate high-quality, conversion-focused copy.
    """
    
    @staticmethod
    def hero_section_prompt(business: BusinessProfile) -> str:
        """
        Generate a prompt for creating compelling hero section copy.
        The hero section is the first thing visitors see and must capture attention.
        """
        return f"""Create a compelling hero section for a local business website with the following specifications:

Business Details:
- Business Name: {business.business_name}
- Business Type: {business.business_type}
- Location: {business.location}
- Target Audience: {business.target_audience}
- Unique Value Proposition: {business.unique_value_proposition}

Brand Voice: {business.brand_voice}

Requirements:
1. Write a powerful headline (8-12 words) that immediately communicates the main benefit
2. Create a supporting subheadline (15-25 words) that elaborates on the value proposition
3. Include a clear call-to-action button text (2-4 words)
4. The copy should be locally relevant and mention {business.location}
5. Focus on customer benefits, not just features
6. Use {business.brand_voice} tone throughout

Format the output as:
HEADLINE: [your headline]
SUBHEADLINE: [your subheadline]
CTA: [your call-to-action]"""

    @staticmethod
    def about_section_prompt(business: BusinessProfile) -> str:
        """
        Generate a prompt for creating an authentic about section.
        This establishes trust and credibility with potential customers.
        """
        return f"""Write an engaging "About Us" section for a local business website:

Business Context:
- Business Name: {business.business_name}
- Business Type: {business.business_type}
- Location: {business.location}
- Years in Business: {business.years_in_business}
- Target Audience: {business.target_audience}

Brand Voice: {business.brand_voice}

Requirements:
1. Write 2-3 paragraphs (150-200 words total) that tell the business story
2. Emphasize the {business.years_in_business} years of experience and local expertise
3. Connect emotionally with {business.target_audience}
4. Highlight community involvement and local commitment
5. Build trust and credibility
6. Use a {business.brand_voice} tone
7. End with a statement that reinforces their commitment to customers

The copy should feel authentic and personal, not corporate or generic."""

    @staticmethod
    def services_section_prompt(business: BusinessProfile) -> str:
        """
        Generate a prompt for creating detailed service descriptions.
        Each service should be presented with benefits, not just features.
        """
        services_list = "\n".join([f"- {service}" for service in business.services])
        benefits_list = "\n".join([f"- {benefit}" for benefit in business.key_benefits]) if business.key_benefits else "Not specified"
        
        return f"""Create compelling service descriptions for a local business website:

Business Information:
- Business Name: {business.business_name}
- Business Type: {business.business_type}
- Location: {business.location}

Services to describe:
{services_list}

Key Benefits to Highlight:
{benefits_list}

Brand Voice: {business.brand_voice}

Requirements:
1. For each service, write:
   - A catchy service title (if needed, improve upon the basic name)
   - A description (40-60 words) focusing on customer benefits
   - 2-3 bullet points highlighting specific advantages
2. Use benefit-driven language (what customers gain, not just what you do)
3. Include local relevance where appropriate
4. Maintain {business.brand_voice} tone throughout
5. Make each service sound valuable and necessary

Format each service as:
SERVICE NAME: [title]
DESCRIPTION: [benefit-focused description]
BENEFITS:
- [benefit 1]
- [benefit 2]
- [benefit 3]"""

    @staticmethod
    def testimonial_prompt_guide(business: BusinessProfile) -> str:
        """
        Generate a prompt that helps create authentic-sounding testimonial placeholders
        or guides for collecting real testimonials.
        """
        pain_points = "\n".join([f"- {point}" for point in business.customer_pain_points]) if business.customer_pain_points else "Not specified"
        
        return f"""Create a guide for testimonials that would resonate on this business website:

Business Context:
- Business Name: {business.business_name}
- Business Type: {business.business_type}
- Target Audience: {business.target_audience}
- Location: {business.location}

Customer Pain Points:
{pain_points}

Requirements:
1. Suggest 3 testimonial themes that would be most impactful
2. For each theme, provide:
   - What aspect of service it should highlight
   - The emotional transformation (before/after)
   - Specific results or outcomes mentioned
   - Why it would resonate with {business.target_audience}
3. Include guidance on local credibility markers (neighborhood, local landmarks)
4. Suggest questions to ask customers to gather these testimonials

This will help the business collect authentic testimonials that convert visitors."""

    @staticmethod
    def cta_section_prompt(business: BusinessProfile) -> str:
        """
        Generate a prompt for creating persuasive call-to-action sections.
        CTAs are critical for conversion and must be compelling.
        """
        return f"""Create a persuasive call-to-action (CTA) section for a local business website:

Business Details:
- Business Name: {business.business_name}
- Business Type: {business.business_type}
- Location: {business.location}
- Target Audience: {business.target_audience}
- Main CTA: {business.call_to_action}

Contact Information:
- Phone: {business.phone or 'To be added'}
- Email: {business.email or 'To be added'}

Brand Voice: {business.brand_voice}

Requirements:
1. Write a compelling CTA headline (6-10 words) that creates urgency or desire
2. Create supporting copy (25-40 words) that:
   - Addresses any last objections
   - Reinforces the main benefit
   - Makes taking action feel easy and risk-free
3. Suggest 2 alternative CTA button texts that drive action
4. Include a trust-building statement (local guarantee, free consultation, etc.)
5. Use {business.brand_voice} tone

Format as:
CTA HEADLINE: [headline]
SUPPORTING COPY: [supporting text]
PRIMARY BUTTON: {business.call_to_action}
ALTERNATIVE BUTTONS:
- [option 1]
- [option 2]
TRUST STATEMENT: [trust-building element]"""

    @staticmethod
    def meta_description_prompt(business: BusinessProfile) -> str:
        """
        Generate a prompt for creating SEO-optimized meta descriptions.
        """
        return f"""Write an SEO-optimized meta description for a local business website:

Business Information:
- Business Name: {business.business_name}
- Business Type: {business.business_type}
- Location: {business.location}
- Unique Value Proposition: {business.unique_value_proposition}
- Main Services: {', '.join(business.services[:3])}

Requirements:
1. Length: 150-160 characters (this is critical for SEO)
2. Include the business location for local SEO
3. Include primary keyword (business type + location)
4. Include a compelling benefit or unique value proposition
5. Include a subtle call-to-action
6. Make it click-worthy while being accurate

Provide 2 variations to choose from."""


class WebsiteCopyGenerator:
    """
    Main generator class that orchestrates the creation of complete website copy
    using structured prompts.
    """
    
    def __init__(self, business_profile: BusinessProfile):
        """
        Initialize the generator with a business profile.
        
        Args:
            business_profile: BusinessProfile object containing business information
        """
        self.business = business_profile
        self.templates = PromptTemplates()
    
    def generate_all_prompts(self) -> Dict[str, str]:
        """
        Generate all prompts for every section of the website.
        
        Returns:
            Dictionary mapping section names to their respective prompts
        """
        return {
            "hero_section": self.templates.hero_section_prompt(self.business),
            "about_section": self.templates.about_section_prompt(self.business),
            "services_section": self.templates.services_section_prompt(self.business),
            "testimonial_guide": self.templates.testimonial_prompt_guide(self.business),
            "cta_section": self.templates.cta_section_prompt(self.business),
            "meta_description": self.templates.meta_description_prompt(self.business)
        }
    
    def generate_section_prompt(self, section: str) -> str:
        """
        Generate a prompt for a specific section.
        
        Args:
            section: Name of the section (hero, about, services, testimonial, cta, meta)
        
        Returns:
            The generated prompt for that section
        """
        prompt_methods = {
            "hero": self.templates.hero_section_prompt,
            "about": self.templates.about_section_prompt,
            "services": self.templates.services_section_prompt,
            "testimonial": self.templates.testimonial_prompt_guide,
            "cta": self.templates.cta_section_prompt,
            "meta": self.templates.meta_description_prompt
        }
        
        if section not in prompt_methods:
            raise ValueError(f"Unknown section: {section}. Valid sections: {list(prompt_methods.keys())}")
        
        return prompt_methods[section](self.business)
    
    def export_prompts(self, filepath: str) -> None:
        """
        Export all prompts to a JSON file for easy use with AI tools.
        
        Args:
            filepath: Path to save the JSON file
        """
        prompts = self.generate_all_prompts()
        
        export_data = {
            "business_profile": {
                "name": self.business.business_name,
                "type": self.business.business_type,
                "location": self.business.location
            },
            "prompts": prompts,
            "instructions": "Use each prompt with an AI copywriting tool (like ChatGPT, Claude, etc.) to generate professional website copy for this business."
        }
        
        with open(filepath, 'w') as f:
            json.dump(export_data, f, indent=2)
        
        print(f"Prompts exported successfully to {filepath}")
    
    def print_prompts(self) -> None:
        """
        Print all prompts in a formatted, readable way.
        """
        prompts = self.generate_all_prompts()
        
        print("=" * 80)
        print(f"WEBSITE COPY PROMPTS FOR: {self.business.business_name}")
        print("=" * 80)
        print()
        
        for section_name, prompt in prompts.items():
            print(f"\n{'=' * 80}")
            print(f"SECTION: {section_name.upper().replace('_', ' ')}")
            print("=" * 80)
            print()
            print(prompt)
            print()


def create_example_business() -> BusinessProfile:
    """
    Create an example business profile for demonstration purposes.
    
    Returns:
        A sample BusinessProfile for a local plumbing business
    """
    return BusinessProfile(
        business_name="Swift Flow Plumbing",
        business_type="Plumbing Services",
        location="Austin, TX",
        years_in_business=15,
        unique_value_proposition="24/7 emergency service with guaranteed same-day response for Austin homeowners",
        target_audience="homeowners in Austin who need reliable, professional plumbing services",
        services=[
            "Emergency Plumbing Repairs",
            "Drain Cleaning & Unclogging",
            "Water Heater Installation & Repair",
            "Leak Detection & Repair",
            "Bathroom & Kitchen Remodeling"
        ],
        key_benefits=[
            "24/7 emergency availability",
            "Licensed and insured technicians",
            "Upfront pricing with no hidden fees",
            "Same-day service guaranteed",
            "10-year warranty on installations"
        ],
        customer_pain_points=[
            "Need urgent help with plumbing emergencies",
            "Worried about being overcharged",
            "Difficulty finding reliable plumbers",
            "Concerned about quality of work"
        ],
        brand_voice="professional yet approachable, emphasizing reliability and trust",
        call_to_action="Call Now for Fast Service",
        phone="(512) 555-0199",
        email="service@swiftflowplumbing.com"
    )


if __name__ == "__main__":
    # Demonstration of the prompt system
    print("=" * 80)
    print("STRUCTURED PROMPT SYSTEM FOR LOCAL BUSINESS WEBSITE COPY")
    print("=" * 80)
    print()
    print("This system generates professional-grade prompts that can be used with")
    print("AI copywriting tools to create complete website copy for local businesses.")
    print()
    
    # Create example business
    example_business = create_example_business()
    
    # Initialize the generator
    generator = WebsiteCopyGenerator(example_business)
    
    # Display all prompts
    generator.print_prompts()
    
    # Export to file
    print("\n" + "=" * 80)
    print("EXPORTING PROMPTS")
    print("=" * 80)
    generator.export_prompts("website_copy_prompts.json")
    
    print("\n" + "=" * 80)
    print("USAGE INSTRUCTIONS")
    print("=" * 80)
    print("""
To use this system for your business:

1. Create a BusinessProfile with your business information
2. Initialize WebsiteCopyGenerator with your profile
3. Generate prompts using generate_all_prompts() or generate_section_prompt()
4. Copy each prompt to your preferred AI tool (ChatGPT, Claude, etc.)
5. Review and customize the generated copy for your website

Example code:
    my_business = BusinessProfile(
        business_name="Your Business Name",
        business_type="Your Business Type",
        location="Your City, State",
        ...
    )
    
    generator = WebsiteCopyGenerator(my_business)
    generator.print_prompts()
    generator.export_prompts("my_prompts.json")
""")
