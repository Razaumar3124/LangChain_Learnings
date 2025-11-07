# import os
# import requests
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.messages import HumanMessage
# from langchain_core.tools import tool, InjectedToolArg
# from typing import Annotated
# from dotenv import load_dotenv

# load_dotenv()

# @tool
# def get_conversion_factor(base_currency: str, target_currency: str) -> float:
#     """This function fetches the currency conversion factor between a given base currency and a target currency"""
    
#     url = f"https://v6.exchangerate-api.com/v6/c2952fe3f4f0a19ca3a4d9c1/pair/{base_currency}/{target_currency}"
    
#     response = requests.get(url)
    
#     return response.json()

# # print(get_conversion_factor.invoke({"base_currency": "USD", "target_currency": "INR"}))

# @tool
# def convert(base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
#     """Given a currency conversion rate this function calculates the target currency value from a given base currency value"""

#     return base_currency_value * conversion_rate

# # print(convert.invoke({"base_currency_value": 10, "conversion_rate": 85.16}))

# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# model_with_tools = model.bind_tools([get_conversion_factor, convert])

# messages = [HumanMessage("what is the conversion factor between USD and INR, and based on that can you convert 10 usd to inr")]

# ai_message = model_with_tools.invoke(messages)

# print(ai_message.tool_calls[0])


import os
import requests
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool
from dotenv import load_dotenv

load_dotenv()

# --- Tool Definitions ---

@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> dict:
    """This function fetches the currency conversion factor between a given base currency and a target currency. Returns a JSON dictionary."""
    
    # NOTE: In a real application, you'd handle API key security better.
    # The API key below is for demonstration and might become invalid.
    url = f"https://v6.exchangerate-api.com/v6/c2952fe3f4f0a19ca3a4d9c1/pair/{base_currency}/{target_currency}"
    
    response = requests.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    
    return response.json()

@tool
def convert(base_currency_value: float, conversion_rate: float) -> float:
    """Given a currency conversion rate this function calculates the target currency value from a given base currency value."""

    return base_currency_value * conversion_rate

# --- Model Setup ---

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
tools = [get_conversion_factor, convert]
model_with_tools = model.bind_tools(tools)

# --- Tool Execution Loop ---

messages = [HumanMessage("what is the conversion factor betweem INR and USD, and based on that can you convert 10 inr to usd")]
print(f"User Message: {messages[0].content}\n")

# 1. First Model Invocation (Model asks for rate)
ai_message_step_1 = model_with_tools.invoke(messages)
messages.append(ai_message_step_1)

print("--- Step 1: Model response (Requesting rate) ---")
print(ai_message_step_1)
print("-" * 50)


# Check if the model requested a tool call
if ai_message_step_1.tool_calls:
    tool_call_step_1 = ai_message_step_1.tool_calls[0]
    tool_name = tool_call_step_1['name']
    tool_args = tool_call_step_1['args']
    tool_id = tool_call_step_1['id']
    
    # Execute the requested tool (get_conversion_factor)
    if tool_name == 'get_conversion_factor':
        print(f"Executing Tool 1: {tool_name}({tool_args})")
        # Find the actual tool function to invoke
        tool_func = next(t for t in tools if t.name == tool_name)
        tool_output_step_1 = tool_func.invoke(tool_args)
        
        # Extract the conversion rate for the next step
        conversion_rate = tool_output_step_1['conversion_rate']
        
        # Prepare the ToolMessage with the output
        tool_message_step_1 = ToolMessage(
            tool_call_id=tool_id,
            content=str(tool_output_step_1), # Send the full JSON output back
        )
        messages.append(tool_message_step_1)
        
        print(f"Tool 1 Output (Rate: {conversion_rate}) added to messages.")
        print("-" * 50)
        
        # 2. Second Model Invocation (Model performs conversion)
        ai_message_step_2 = model_with_tools.invoke(messages)
        messages.append(ai_message_step_2)

        print("--- Step 2: Model response (Requesting conversion) ---")
        print(ai_message_step_2)
        print("-" * 50)
        
        # Check if the model requested the second tool call (convert)
        if ai_message_step_2.tool_calls:
            tool_call_step_2 = ai_message_step_2.tool_calls[0]
            tool_name_2 = tool_call_step_2['name']
            tool_args_2 = tool_call_step_2['args']
            tool_id_2 = tool_call_step_2['id']

            if tool_name_2 == 'convert':
                print(f"Executing Tool 2: **{tool_name_2}({tool_args_2})**")
                # Find the actual tool function to invoke
                tool_func_2 = next(t for t in tools if t.name == tool_name_2)
                tool_output_step_2 = tool_func_2.invoke(tool_args_2)

                print(f"\n✅ Final Conversion Result: 10 USD = **{tool_output_step_2:.2f} INR**")
                
                # If you wanted the final conversational response, you'd do a third invoke
                # after sending the final ToolMessage back.
            else:
                print(f"Model called unexpected tool: {tool_name_2}")
        else:
            print("Model did not call a second tool. It might have given a final answer.")
    else:
        print(f"Model called unexpected tool in step 1: {tool_name}")
else:
    print("Model did not call any tool.")