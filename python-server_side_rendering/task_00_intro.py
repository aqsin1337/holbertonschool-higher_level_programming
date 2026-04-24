import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for idx, attendee in enumerate(attendees, start=1):
        output_content = template
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            val = attendee.get(placeholder) or "N/A"
            output_content = output_content.replace(f"{{{placeholder}}}", str(val))
        
        with open(f"output_{idx}.txt", "w") as f:
            f.write(output_content)
