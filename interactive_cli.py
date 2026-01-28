#!/usr/bin/env python3
"""
Interactive CLI for generating website copy prompts for local businesses.
This tool guides users through creating a business profile and generating prompts.
"""

from prompt_system import BusinessProfile, WebsiteCopyGenerator
import sys


def print_header(text: str) -> None:
    """Print a formatted header."""
    print("\n" + "=" * 80)
    print(text.center(80))
    print("=" * 80 + "\n")


def get_input(prompt: str, default: str = None, required: bool = True) -> str:
    """Get user input with optional default value."""
    if default:
        prompt = f"{prompt} [{default}]: "
    else:
        prompt = f"{prompt}: "
    
    while True:
        value = input(prompt).strip()
        if value:
            return value
        elif default:
            return default
        elif not required:
            return ""
        else:
            print("This field is required. Please enter a value.")


def get_list_input(prompt: str, min_items: int = 1) -> list:
    """Get a list of items from user input."""
    print(f"\n{prompt}")
    print("Enter one item per line. Type 'done' when finished.")
    
    items = []
    counter = 1
    while True:
        item = input(f"  {counter}. ").strip()
        if item.lower() == 'done':
            if len(items) >= min_items:
                break
            else:
                print(f"Please enter at least {min_items} item(s).")
        elif item:
            items.append(item)
            counter += 1
    
    return items


def get_int_input(prompt: str, default: int = None) -> int:
    """Get integer input from user."""
    while True:
        if default:
            value = input(f"{prompt} [{default}]: ").strip()
            if not value:
                return default
        else:
            value = input(f"{prompt}: ").strip()
        
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid number.")


def create_business_profile_interactive() -> BusinessProfile:
    """Guide user through creating a business profile interactively."""
    print_header("BUSINESS INFORMATION")
    
    print("Let's gather information about your business to generate high-quality copy prompts.\n")
    
    # Required fields
    business_name = get_input("Business Name")
    business_type = get_input("Business Type (e.g., Restaurant, Law Firm, Plumbing)")
    location = get_input("Location (City, State)")
    years_in_business = get_int_input("Years in Business")
    unique_value_proposition = get_input("Unique Value Proposition\n  (What makes you different from competitors)")
    target_audience = get_input("Target Audience\n  (Who are your ideal customers)")
    
    services = get_list_input("List your main services/offerings", min_items=3)
    
    # Optional fields
    print("\n--- OPTIONAL: Additional Details (Press Enter to skip) ---\n")
    
    key_benefits = []
    add_benefits = get_input("Add key benefits/advantages? (y/n)", default="y", required=False)
    if add_benefits.lower() == 'y':
        key_benefits = get_list_input("List key benefits you provide", min_items=0)
    
    customer_pain_points = []
    add_pain_points = get_input("Add customer pain points? (y/n)", default="y", required=False)
    if add_pain_points.lower() == 'y':
        customer_pain_points = get_list_input("List problems your customers face", min_items=0)
    
    brand_voice = get_input("Brand Voice/Tone", 
                           default="professional and friendly",
                           required=False)
    
    call_to_action = get_input("Main Call-to-Action", 
                              default="Contact us today",
                              required=False)
    
    phone = get_input("Phone Number", required=False)
    email = get_input("Email Address", required=False)
    website = get_input("Website URL", required=False)
    
    # Create and return the profile
    return BusinessProfile(
        business_name=business_name,
        business_type=business_type,
        location=location,
        years_in_business=years_in_business,
        unique_value_proposition=unique_value_proposition,
        target_audience=target_audience,
        services=services,
        key_benefits=key_benefits,
        customer_pain_points=customer_pain_points,
        brand_voice=brand_voice or "professional and friendly",
        call_to_action=call_to_action or "Contact us today",
        phone=phone or None,
        email=email or None,
        website=website or None
    )


def select_sections() -> list:
    """Let user select which sections to generate prompts for."""
    print_header("SELECT SECTIONS")
    
    sections = {
        "1": ("hero", "Hero Section (headline, subheadline, CTA)"),
        "2": ("about", "About Us Section"),
        "3": ("services", "Services Section"),
        "4": ("testimonial", "Testimonial Collection Guide"),
        "5": ("cta", "Call-to-Action Section"),
        "6": ("meta", "Meta Description (SEO)")
    }
    
    print("Which sections would you like to generate prompts for?\n")
    for key, (_, description) in sections.items():
        print(f"  {key}. {description}")
    print("  7. All sections")
    print("  0. Exit\n")
    
    choice = get_input("Enter your choice (or comma-separated choices like 1,3,5)")
    
    if choice == "0":
        return []
    elif choice == "7":
        return [section for section, _ in sections.values()]
    else:
        selected = []
        for c in choice.split(","):
            c = c.strip()
            if c in sections:
                selected.append(sections[c][0])
        return selected


def display_prompt(section: str, prompt: str) -> None:
    """Display a single prompt in a formatted way."""
    print_header(f"{section.upper().replace('_', ' ')} PROMPT")
    print(prompt)
    print("\n" + "-" * 80)


def main():
    """Main CLI application."""
    print_header("WEBSITE COPY PROMPT GENERATOR")
    print("Generate professional prompts for AI-powered website copywriting")
    print("Perfect for web agencies, copywriters, and business owners\n")
    
    try:
        # Create business profile
        business = create_business_profile_interactive()
        
        # Initialize generator
        generator = WebsiteCopyGenerator(business)
        
        # Select sections
        sections = select_sections()
        
        if not sections:
            print("\nNo sections selected. Exiting.")
            return
        
        # Generate and display prompts
        print_header("GENERATED PROMPTS")
        print(f"Business: {business.business_name}")
        print(f"Sections: {len(sections)}\n")
        
        input("Press Enter to view prompts...")
        
        for section in sections:
            prompt = generator.generate_section_prompt(section)
            display_prompt(section, prompt)
            
            if section != sections[-1]:  # If not the last one
                input("\nPress Enter for next prompt...")
        
        # Export option
        print_header("EXPORT PROMPTS")
        export = get_input("Export all prompts to JSON file? (y/n)", default="y", required=False)
        
        if export.lower() == 'y':
            filename = get_input("Filename", 
                               default=f"{business.business_name.replace(' ', '_').lower()}_prompts.json",
                               required=False)
            generator.export_prompts(filename)
            print(f"\n✓ Prompts exported to {filename}")
        
        print_header("NEXT STEPS")
        print("""
1. Copy each prompt to your preferred AI tool (ChatGPT, Claude, etc.)
2. The AI will generate professional copy based on your business information
3. Review and customize the generated copy
4. Use the copy on your website

Thank you for using the Website Copy Prompt Generator!
        """)
        
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nError: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
