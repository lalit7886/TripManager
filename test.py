from backend import run_travel_agent


user_input = input("Enter travel request: ")

res = run_travel_agent(
    user_input,
    thread_id="test_user"
)
print(res)