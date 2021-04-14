defmodule WordCount do
  @doc """
  Count the number of words in the sentence.

  Words are compared case-insensitively.
  """
  @spec count(String.t()) :: map
  def count(sentence) do
    list = String.downcase(sentence) |> String.replace(~r/[^[:alnum:]-]/u, " ") |> String.split([" ", ",", "_"], trim: true )
    Enum.reduce(list, %{}, fn y, acc -> Map.update(acc, y, 1, &(&1 + 1)) end)
  end
end
