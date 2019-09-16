<script src="https://cdnjs.cloudflare.com/ajax/libs/tablefilter/2.5.0/tablefilter.js"></script>

<h1>TableFilter starter</h1>
https://cdnjs.cloudflare.com/ajax/libs/tablefilter/2.5.0/filtergrid.css

<table id="demo">
    <thead>
        <tr>
            <th>country</th>
            <th>isocode</th>
            <th>year</th>
            <th>POP</th>
            <th>XRAT</th>
            <th>PPP</th>
            <th>cgdp</th>
            <th>cc</th>
            <th>ci</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Benin</td>
            <td>BEN</td>
            <td>1998</td>
            <td>5950.33</td>
            <td>589.9517822</td>
            <td>190.95</td>
            <td>1178.46</td>
            <td>90.98</td>
            <td>7.55</td>
        </tr>
        <tr>
            <td>Benin</td>
            <td>BEN</td>
            <td>1999</td>
            <td>6109.53</td>
            <td>615.6990967</td>
            <td>200.19</td>
            <td>1174.90</td>
            <td>92.61</td>
            <td>7.86</td>
        </tr>
        <tr>
            <td>Benin</td>
            <td>BEN</td>
            <td>2000</td>
            <td>6272.00</td>
            <td>711.9763184</td>
            <td>200.61</td>
            <td>1224.74</td>
            <td>92.27</td>
            <td>8.25</td>
        </tr>
        <tr>
            <td>Burkina Faso</td>
            <td>BFA</td>
            <td>1994</td>
            <td>9755.03</td>
            <td>555.2047119</td>
            <td>125.76</td>
            <td>838.76</td>
            <td>79.81</td>
            <td>6.57</td>
        </tr>
    </tbody>
</table>

<script type="text/javascript">
var filtersConfig = {
  // instruct TableFilter location to import ressources from
  base_path: 'https://unpkg.com/tablefilter@latest/dist/tablefilter/',
  col_1: 'select',
  col_2: 'select',
  col_3: 'select',
  alternate_rows: true,
  rows_counter: true,
  btn_reset: true,
  loader: true,
  mark_active_columns: true,
  highlight_keywords: true,
  no_results_message: true,
  col_types: [
    'string', 'string', 'number',
    'number', 'number', 'number',
    'number', 'number', 'number'
  ],
  custom_options: {
    cols: [3],
    texts: [
      [
        '0 - 25 000',
        '100 000 - 1 500 000'
      ]
    ],
    values: [
      [
        '>0 && <=25000',
        '>100000 && <=1500000'
      ]
    ],
    sorts: [false]
  },
  col_widths: [
    '150px', '100px', '100px',
    '70px', '100px', '70px',
    '70px', '60px', '60px'
  ],
  extensions: [{
    name: 'sort',
    images_path: 'https://unpkg.com/tablefilter@latest/dist/tablefilter/style/themes/'
  }]
};

var tf = new TableFilter('demo', filtersConfig);
tf.init();
</script>