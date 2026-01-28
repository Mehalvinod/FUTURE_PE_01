# Quick Start Guide

Get professional website copy for your local business in 3 simple steps!

## Step 1: Choose Your Method

### Option A: Use the Example (Fastest)
Perfect for understanding how the system works.

```bash
python prompt_system.py
```

This shows you a complete example and creates `website_copy_prompts.json`.

### Option B: Interactive Mode (Easiest)
Guided step-by-step process for your business.

```bash
python interactive_cli.py
```

Answer the questions and get your custom prompts!

### Option C: Code It Yourself (Most Flexible)
Full control over your business profile.

```python
from prompt_system import BusinessProfile, WebsiteCopyGenerator

# Define your business
my_business = BusinessProfile(
    business_name="Your Business Name",
    business_type="What you do",
    location="City, State",
    years_in_business=5,
    unique_value_proposition="What makes you special",
    target_audience="Who you serve",
    services=["Service 1", "Service 2", "Service 3"]
)

# Generate prompts
generator = WebsiteCopyGenerator(my_business)
generator.print_prompts()
generator.export_prompts("my_prompts.json")
```

## Step 2: Use the Prompts with AI

1. Open the generated JSON file or copy from console output
2. Go to ChatGPT, Claude, or your preferred AI tool
3. Copy and paste each prompt one at a time
4. The AI will generate professional copy for each section

### Example Workflow:

```
You: [Paste Hero Section Prompt]

AI: [Generates headline, subheadline, and CTA]

You: [Paste About Section Prompt]

AI: [Generates about us copy]

... repeat for all sections
```

## Step 3: Review and Deploy

1. **Review**: Read through the generated copy
2. **Customize**: Adjust any details specific to your business
3. **Deploy**: Add the copy to your website
4. **Test**: A/B test different variations

## Tips for Best Results

### 1. Be Specific in Your Business Profile
❌ **Generic:** "Quality service"  
✅ **Specific:** "Same-day service with 24/7 availability"

### 2. Know Your Audience
❌ **Vague:** "Everyone who needs plumbing"  
✅ **Targeted:** "Homeowners in Austin who need reliable emergency plumbing"

### 3. List Real Benefits
❌ **Features:** "Licensed plumbers"  
✅ **Benefits:** "Licensed plumbers so you're protected and guaranteed quality work"

### 4. Include Pain Points
Understanding customer problems helps generate solution-focused copy:
- "Worried about being overcharged"
- "Need urgent help"
- "Can't find reliable service"

### 5. Define Your Voice
- "Professional and trustworthy"
- "Friendly and approachable"
- "Passionate and knowledgeable"
- "Warm and family-oriented"

## Common Use Cases

### Web Agency
Generate prompts for 10 clients in an hour:
```python
for client in client_list:
    gen = WebsiteCopyGenerator(client)
    gen.export_prompts(f"{client.business_name}_prompts.json")
```

### Business Owner
Get professional copy without hiring an agency:
```bash
python interactive_cli.py
# Follow the prompts
# Use output with ChatGPT
# Save thousands of dollars
```

### Freelance Copywriter
Streamline your workflow:
```python
# Create profile from client brief
# Generate structured prompts
# Use prompts to guide copywriting
# Deliver faster, more consistent results
```

## Troubleshooting

### Problem: Prompts seem generic
**Solution:** Add more specific details to your BusinessProfile, especially:
- Unique value proposition
- Customer pain points
- Key benefits
- Specific services

### Problem: Generated copy doesn't match my brand
**Solution:** Adjust the `brand_voice` field to be more specific:
- ❌ "Professional"
- ✅ "Professional yet warm, like a trusted family advisor"

### Problem: Want different copy variations
**Solution:** Run the prompts multiple times with the AI, or adjust the business profile slightly and regenerate.

### Problem: Need additional sections
**Solution:** The system covers the core 6 sections. For additional sections (FAQ, Team, Contact), you can create similar prompts following the same pattern shown in `prompt_system.py`.

## Next Steps

1. ✅ Generate your prompts
2. ✅ Create copy with AI
3. 📸 See results on your website
4. 📈 Track conversions and optimize

## Need Help?

- Check `EXAMPLES.md` for 5 complete business examples
- Review `SAMPLE_OUTPUT.md` to see what good copy looks like
- Read `README_PROMPT_SYSTEM.md` for complete documentation

## Time Savings

Traditional Process:
- Hiring copywriter: 1-2 weeks + $2,000-$5,000
- Multiple revision rounds: 1-2 weeks
- **Total: 2-4 weeks, $2,000-$5,000**

This System:
- Generate prompts: 5-10 minutes
- Create copy with AI: 10-15 minutes
- Review and customize: 10-20 minutes
- **Total: 25-45 minutes, $0**

---

**Ready to get started? Run `python prompt_system.py` now!**
