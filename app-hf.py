import gradio as gr
import requests
import json

def call_pathlet_api(birth_date, birth_time, birth_location, service):
    """
    Generic function to call Pathlet API endpoints
    """
    base_url = "https://pathlet-api.vercel.app"  # Replace with actual API URL
    
    payload = {
        "birth_date": birth_date,
        "birth_time": birth_time,
        "birth_location": birth_location
    }
    
    endpoints = {
        "Ascendant": "/get_ascendants",
        "Numerology": "/calculate_numerology",
        "Human Design": "/calculate_human_design"
    }
    
    try:
        response = requests.post(
            f"{base_url}{endpoints[service]}", 
            json=payload, 
            timeout=10
        )
        response.raise_for_status()
        return json.dumps(response.json(), indent=2)
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# Pathlet: Personal Insights API")
    
    with gr.Row():
        birth_date = gr.Textbox(label="Birth Date (YYYY-MM-DD)")
        birth_time = gr.Textbox(label="Birth Time (Optional)", placeholder="HH:MM AM/PM")
        birth_location = gr.Textbox(label="Birth Location")
    
    service = gr.Dropdown(
        ["Ascendant", "Numerology", "Human Design"], 
        label="Select Insight Type"
    )
    
    submit = gr.Button("Get Insights")
    output = gr.Textbox(label="Results")
    
    submit.click(
        fn=call_pathlet_api, 
        inputs=[birth_date, birth_time, birth_location, service], 
        outputs=output
    )

demo.launch()
