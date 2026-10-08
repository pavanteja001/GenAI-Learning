# bmi cal it is seq_workflow takes height, weight and cal bmi
# i/p height, weight
# flow-> START-> cal_BMI -> lable -> END
# NOTES AT BOTTOM

from langgraph.graph import START, StateGraph, END
from typing import TypedDict


class BMIState(TypedDict):
    weight_kg: float
    height_m: float
    bmi: float
    category: str


def calculate_bmi(state: BMIState) -> BMIState:
    weight = state["weight_kg"]
    height = state["height_m"]
    bmi = weight / (height**2)
    state["bmi"] = round(bmi, 2)
    return state


def label_bmi(state: BMIState) -> BMIState:
    bmi = state["bmi"]
    if bmi < 18.5:
        state["category"] = "Underweight"
    elif 18.5 <= bmi < 25:
        state["category"] = "Normal"
    elif 25 <= bmi < 30:
        state["category"] = "Overweight"
    else:
        state["category"] = "Obese"
    return state


graph = StateGraph(BMIState)

# add nodes to graph -> compile -> execute

graph.add_node("calculate_bmi", calculate_bmi)
graph.add_node("label_bmi", label_bmi)


# create edges
graph.add_edge(START, "calculate_bmi")
graph.add_edge("calculate_bmi", "label_bmi")
graph.add_edge("label_bmi", END)

# compile the workflow
workflow = graph.compile()

# execute the graph
intial_state = {"weight_kg": 80, "height_m": 1.73}

final_state = workflow.invoke(intial_state)
print(final_state)


"""
Here are consolidated notes from the last two topics.

## `add_node` parameters

The call: `graph.add_node("calculate_bmi", calculate_bmi)`

**First argument — node name (string): `"calculate_bmi"`**
- The identifier/label for the node inside the graph; think of it as the node's address.
- It's how you refer to the node everywhere else, most importantly in `add_edge` (e.g. `graph.add_edge(START, "calculate_bmi")`).
- Must be unique within the graph.
-The name is optional. If you pass just the function, LangGraph uses the function's __name__ as the node name:
pythongraph.add_node(calculate_bmi)
# node name becomes "calculate_bmi" automatically


**Second argument — the runnable (your function): `calculate_bmi`**
- The actual work the node performs.
- When the graph reaches this node, it calls this function, passing in the current state.
- The function returns a (partial) state update, which LangGraph merges back into the state.
- You pass the function *object* (no parentheses) — handing LangGraph the function so it can call it later.

Conceptual model: `add_node(name, what_to_run)`.

**Extra points worth knowing:**
- **The name is optional.** Passing just the function makes LangGraph use the function's `__name__` as the node name:
  ```python
  graph.add_node(calculate_bmi)   # node name becomes "calculate_bmi" automatically
  ```
  This is why many tutorials use one argument. Being explicit with a string is clearer and lets you name the node differently from the function.
- **The signature is overloaded.** Depending on the LangGraph version, `add_node` accepts several forms — `add_node(action)`, `add_node(name, action)`, plus optional keyword args like `metadata` and `retry_policy`. The two-positional-arg form is the standard one.

## Why the 2nd argument is `calculate_bmi`, not `calculate_bmi()`

`calculate_bmi` and `calculate_bmi()` are completely different things in Python:
- `calculate_bmi` — the function **object** itself, uncalled. LangGraph holds onto it and decides *when* to run it.
- `calculate_bmi()` — **runs the function right now** and gives LangGraph whatever it *returns*, not the function.

**Key idea:** in Python, functions are values you can pass around like a number or string. Name without `()` = passing the function itself. Name with `()` = "execute it and give me the result."

**Why running it now would break:**
- The function needs `state` to do its job (`weight = state["weight_kg"]`, etc.).
- Writing `calculate_bmi()` at graph-build time runs it immediately, but there's no `state` to pass, causing:
  ```
  TypeError: calculate_bmi() missing 1 required positional argument: 'state'
  ```
- Even if it didn't error, you'd be storing the *return value* in the node, not the function — so the node would have nothing to execute later.

**The timing is the whole point:**
- When you build the graph, the work hasn't happened yet. The state doesn't exist until you call `workflow.invoke(initial_state)`.
- LangGraph needs the function uncalled so that later — at the right moment, with the real state in hand — it can do:
  ```python
  new_state = calculate_bmi(current_state)   # LangGraph calls it for you, passing state
  ```

**Analogy:** you're giving someone a recipe to cook later, not handing them a finished dish. `calculate_bmi` is the recipe; `calculate_bmi()` is trying to cook it on the spot, but the ingredients (the state) aren't there yet.

**Rule of thumb:** you pass the function; LangGraph calls it. Same reason edges use the node name and never invoke anything themselves.
"""
