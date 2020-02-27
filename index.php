<?php
$conn=mysqli_connect("", "root", ".Zlj20082114");
$db=mysqli_select_db($conn, "stocks");
$query="SELECT * FROM stock";
$rows=mysqli_query($conn, $query);
$ncol=mysqli_num_fields($rows);
echo("<tr>");
?>

<html>
<table border="1">
<tbody>
<tr>
	<th>Symbol</th>
	<th>Name</th>
	<th>Volume</th>
	<th>price</th>
	<th>Change</th>
	<th>%change</th>
</tr>

<?php while($row=mysqli_fetch_array($rows)){ ?>
	<tr>
	<?php for($col=0; $col<$ncol; $col++){ ?>
		<td><?php echo $row[$col]; ?></td>
	<?php } ?>
	</tr>
<?php } ?>
</tbody>
</table>
</html>
