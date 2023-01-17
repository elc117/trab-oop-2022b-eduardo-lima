def test_example(monkeypatch, inputs):
    def mock_input():
        return inputs.pop(0)
    monkeypatch.setattr("builtins.input", mock_input)
    input1 = input()
    assert input1 == "input1"
    input2 = input()
    assert input2 == "input2"