# Example Use Cases

## Example 1: Local Restaurant

```python
from prompt_system import BusinessProfile, WebsiteCopyGenerator

restaurant = BusinessProfile(
    business_name="Bella Italia Trattoria",
    business_type="Italian Restaurant",
    location="San Francisco, CA",
    years_in_business=8,
    unique_value_proposition="Authentic Northern Italian cuisine using family recipes passed down for three generations",
    target_audience="food enthusiasts and families looking for authentic Italian dining experiences",
    services=[
        "Fine Dining",
        "Private Events & Catering",
        "Wine Tasting Events",
        "Cooking Classes"
    ],
    key_benefits=[
        "Authentic recipes from Northern Italy",
        "Locally sourced organic ingredients",
        "Award-winning wine selection",
        "Private dining room available",
        "Family-owned and operated"
    ],
    customer_pain_points=[
        "Difficulty finding authentic Italian food",
        "Looking for special occasion dining",
        "Want to learn authentic Italian cooking",
        "Need reliable catering for events"
    ],
    brand_voice="warm, passionate, and family-oriented with Italian charm",
    call_to_action="Reserve Your Table",
    phone="(415) 555-0188",
    email="info@bellaitalia-sf.com"
)

generator = WebsiteCopyGenerator(restaurant)
generator.export_prompts("bella_italia_prompts.json")
```

## Example 2: Law Firm

```python
from prompt_system import BusinessProfile, WebsiteCopyGenerator

law_firm = BusinessProfile(
    business_name="Martinez & Associates",
    business_type="Personal Injury Law Firm",
    location="Miami, FL",
    years_in_business=20,
    unique_value_proposition="No fees unless we win - aggressive representation with a personal touch for accident victims",
    target_audience="individuals who have been injured in accidents and need legal representation",
    services=[
        "Car Accident Claims",
        "Slip and Fall Cases",
        "Medical Malpractice",
        "Wrongful Death Claims",
        "Workers Compensation"
    ],
    key_benefits=[
        "No fee unless we win your case",
        "24/7 availability for emergencies",
        "Spanish-English bilingual staff",
        "Over $100M recovered for clients",
        "Free initial consultation"
    ],
    customer_pain_points=[
        "Overwhelmed by medical bills after accident",
        "Insurance companies won't pay fair compensation",
        "Don't know their legal rights",
        "Can't afford attorney fees upfront"
    ],
    brand_voice="compassionate yet strong, emphasizing justice and results",
    call_to_action="Get Your Free Consultation",
    phone="(305) 555-0177",
    email="contact@martinezlawfl.com"
)

generator = WebsiteCopyGenerator(law_firm)
generator.export_prompts("martinez_law_prompts.json")
```

## Example 3: Fitness Studio

```python
from prompt_system import BusinessProfile, WebsiteCopyGenerator

fitness_studio = BusinessProfile(
    business_name="CoreFit Studio",
    business_type="Boutique Fitness Studio",
    location="Portland, OR",
    years_in_business=5,
    unique_value_proposition="Small-group training with personalized attention for real, sustainable results",
    target_audience="busy professionals aged 30-50 who want effective workouts without crowded gyms",
    services=[
        "Small Group Training",
        "Personal Training",
        "Nutrition Coaching",
        "Corporate Wellness Programs"
    ],
    key_benefits=[
        "Classes limited to 8 people maximum",
        "Certified trainers with 10+ years experience",
        "Customized workout plans",
        "Results tracking and accountability",
        "Flexible scheduling including early morning and evening"
    ],
    customer_pain_points=[
        "Too busy for long gym sessions",
        "Don't know how to exercise effectively",
        "Lack motivation to work out alone",
        "Want personal attention but can't afford private training"
    ],
    brand_voice="motivating and supportive, focused on sustainable lifestyle change",
    call_to_action="Book Your Free Trial",
    phone="(503) 555-0166",
    email="hello@corefit-pdx.com"
)

generator = WebsiteCopyGenerator(fitness_studio)
generator.export_prompts("corefit_prompts.json")
```

## Example 4: Real Estate Agent

```python
from prompt_system import BusinessProfile, WebsiteCopyGenerator

realtor = BusinessProfile(
    business_name="Sarah Chen Homes",
    business_type="Residential Real Estate",
    location="Seattle, WA",
    years_in_business=12,
    unique_value_proposition="Local market expertise with a tech-savvy approach to finding your perfect home",
    target_audience="first-time homebuyers and families relocating to Seattle",
    services=[
        "Home Buying Assistance",
        "Home Selling Services",
        "Relocation Services",
        "Investment Property Consulting",
        "Virtual Home Tours"
    ],
    key_benefits=[
        "12 years of Seattle market experience",
        "Average 7 days to sell listings",
        "Virtual tour technology for remote buyers",
        "Negotiation expertise that saves clients thousands",
        "Network of trusted local contractors and lenders"
    ],
    customer_pain_points=[
        "Overwhelmed by the home buying process",
        "Don't know Seattle neighborhoods well",
        "Worried about overpaying",
        "Need to buy/sell quickly due to relocation"
    ],
    brand_voice="knowledgeable and reassuring, like a trusted friend who knows real estate",
    call_to_action="Start Your Home Search",
    phone="(206) 555-0155",
    email="sarah@sarahchenhomes.com"
)

generator = WebsiteCopyGenerator(realtor)
generator.export_prompts("sarah_chen_prompts.json")
```

## Example 5: Pet Grooming

```python
from prompt_system import BusinessProfile, WebsiteCopyGenerator

pet_grooming = BusinessProfile(
    business_name="Pawsitive Perfection",
    business_type="Pet Grooming & Spa",
    location="Nashville, TN",
    years_in_business=7,
    unique_value_proposition="Fear-free grooming techniques that keep pets calm and happy",
    target_audience="pet owners who want gentle, stress-free grooming for their dogs and cats",
    services=[
        "Full-Service Grooming",
        "Bath & Brush",
        "Nail Trimming",
        "De-shedding Treatments",
        "Pet Spa Services"
    ],
    key_benefits=[
        "Certified in fear-free grooming methods",
        "Calm, quiet environment (no cage dryers)",
        "One-on-one attention (one pet at a time)",
        "Natural, pet-safe products only",
        "Mobile grooming available"
    ],
    customer_pain_points=[
        "Pet is anxious or scared at groomers",
        "Concerned about pet safety and treatment",
        "Difficult to transport pet to groomer",
        "Want gentle handling for senior or special needs pets"
    ],
    brand_voice="gentle, loving, and understanding - like a pet's best friend",
    call_to_action="Book a Spa Day",
    phone="(615) 555-0144",
    email="hello@pawsitiveperfection.com"
)

generator = WebsiteCopyGenerator(pet_grooming)
generator.export_prompts("pawsitive_perfection_prompts.json")
```

## How to Use These Examples

1. Copy any example that matches your business type
2. Modify the details to match your specific business
3. Run the code to generate prompts
4. Use the prompts with AI tools to create your website copy
