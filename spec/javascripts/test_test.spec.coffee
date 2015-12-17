
describe "A failing test", () ->
  it "should fail", () ->
    expect false
    .toBe true

describe "A passing test", () ->
  it "should pass", () ->
    expect true
    .toBe true
