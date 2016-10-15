# 42-fillit

## Algorithm
Basic Recursive Backtracking
```
if (count_empty_spaces(solution_arr) == g_spaces)
		return (1);
	sa_i = 0;
	while (solution_arr[sa_i])
	{
		if (valid_placement(solution_arr, sa_i, input_arr[ia_i]))
		{
			place_tetri(solution_arr, sa_i, input_arr[ia_i]);
			if (solve(solution_arr, input_arr, ++ia_i))
				return (1);
			remove_tetri(solution_arr, sa_i, input_arr[--ia_i]);
		}
		sa_i++;
	}
```
## Solution Arr
1D array
### Valid Placement
```
static int	offset_detective(int sa_i, int offset, int zero_offset)
{
	offset = offset / 4 * g_size + offset % 4 + sa_i - zero_offset;
	return (offset);
}

int			valid_placement(char *solution_arr, int sa_i, t_offsets tetri)
{
	int		o_i;
	int		offsets[8];

	o_i = 0;
	offsets[0] = offset_detective(sa_i, tetri.offset1, tetri.offset0);
	offsets[1] = offset_detective(sa_i, tetri.offset2, tetri.offset0);
	offsets[2] = offset_detective(sa_i, tetri.offset3, tetri.offset0);
	offsets[3] = 0;
	offsets[4] = tetri.offset1;
	offsets[5] = tetri.offset2;
	offsets[6] = tetri.offset3;
	offsets[7] = 0;
	while (offsets[o_i] != 0)
	{
		if (((offsets[o_i] / g_size - sa_i / g_size) != (offsets[o_i + 4] / 4))
				|| ((offsets[o_i]) >= (g_size * g_size))
				|| solution_arr[sa_i] != '.'
				|| solution_arr[offsets[o_i]] != '.')
			return (0);
		o_i++;
	}
	return (1);
}
```
## Validation
```
static int	count_blocks(char *row)
{
	int		c;
	int		n_blocks;

	c = 0;
	n_blocks = 0;
	while (row[c])
	{
		if (row[c] == '#')
			n_blocks++;
		c++;
	}
	return (n_blocks == 4) ? (1) : (0);
}

static int	touch_detective(char *row)
{
	int		j;
	int		i;
	int		touches;
	int		*b;

	i = 0;
	touches = 0;
	b = block_indexes(row);
	while (i < 4)
	{
		j = 0;
		while (j < 4 && (i != 3 || j != 3))
		{
			if (i == j)
				j++;
			if ((b[i] / 4 == b[j] / 4) && (ABS(b[i] - b[j]) == 1))
				touches++;
			if ((b[i] % 4 == b[j] % 4) && (ABS(b[i] / 4 - b[j] / 4) == 1))
				touches++;
			j++;
		}
		i++;
	}
	free(b);
	return (touches == 6 || touches == 8) ? (1) : (0);
}

int			valid_blocks(char **arr)
{
	int		r;

	r = 0;
	while (r < g_tetriminos)
	{
		if (!count_blocks(arr[r]) || !touch_detective(arr[r]))
			return (0);
		r++;
	}
	return (1);
}

static int	examine_file(int n_lines, int n_chars, int fd, char *buf)
{
	while (read(fd, buf, 1))
	{
		if (NON_VALID(*buf))
			return (0);
		else if (*buf == '\n')
		{
			n_lines++;
			read(fd, buf, 1);
			if (n_chars != 4 || ((*buf == '\n') &&
						(n_lines != 4)) || NON_VALID(*buf))
				return (0);
			n_chars = 0;
			if ((*buf == '\n') && (n_lines == 4))
			{
				n_lines = 0;
				g_tetriminos++;
			}
			else
				n_chars++;
		}
		else
			n_chars++;
	}
	return (*buf == '\n') ? (1) : (0);
}

int			valid_file(int fd)
{
	int		n_lines;
	int		n_chars;
	char	buf[1];

	if (fd == -1)
		return (0);
	n_lines = 0;
	n_chars = 0;
	return (examine_file(n_lines, n_chars, fd, buf) == 0) ? (0) : (1);
}
```
