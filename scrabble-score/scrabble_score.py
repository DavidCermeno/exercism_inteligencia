defmodule Scrabble do
  @doc """
  Calculate the scrabble score for the word.
  """
  @spec score(String.t()) :: non_neg_integer
  def score(word) do
    String.graphemes(word)
    |> Enum.map(&score_letter/1)
    |> Enum.sum
  end

  @spec score_letter(String.grapheme()) :: non_neg_integer
  defp score_letter(letter) do
    case String.upcase(letter) do
      x when x in ~w"A E I O U L N R S T" -> 1
      x when x in ~w"D G" -> 2
      x when x in ~w"B C M P" -> 3
      x when x in ~w"F H V W Y" -> 4
      "K" -> 5
      x when x in ~w"J X" -> 8
      x when x in ~w"Q Z" -> 10
      _ -> 0
    end
  end
end
