<template>
  <h1>Registros de operadoras</h1>
  <span>Exibindo 10 Registros</span>
  <br>
  <br>
  <div class="card">
      <DataTable :value="products" tableStyle="min-width: 50rem">
          <Column field="REGISTRO_OPERADORA" header="REGISTRO_OPERADORA"></Column>
          <Column field="CNPJ" header="CNPJ"></Column>
          <Column field="RAZAO_SOCIAL" header="RAZAO_SOCIAL"></Column>
          <Column field="NOME_FANTASIA" header="NOME_FANTASIA"></Column>
          <Column field="MODALIDADE" header="MODALIDADE"></Column>
          <Column field="LOGRADOURO" header="LOGRADOURO"></Column>
          <Column field="NUMERO" header="NUMERO"></Column>
          <Column field="COMPLEMENTO" header="COMPLEMENTO"></Column>
          <Column field="BAIRRO" header="BAIRRO"></Column>
          <Column field="CIDADE" header="CIDADE"></Column>
          <Column field="UF" header="UF"></Column>
          <Column field="CEP" header="CEP"></Column>
          <Column field="DDD" header="DDD"></Column>
          <Column field="TELEFONE" header="TELEFONE"></Column>
          <Column field="FAX" header="FAX"></Column>
          <Column field="EMAIL" header="EMAIL"></Column>
          <Column field="REPRESENTANTE" header="REPRESENTANTE"></Column>
          <Column field="CARGO_REPRESENTANTE" header="CARGO_REPRESENTANTE"></Column>
          <Column field="REGIAO_COMERCIALIZACAO" header="REGIAO_COMERCIALIZACAO"></Column>
          <Column field="DATA_REGISTRO_ANS" header="DATA_REGISTRO_ANS"></Column>
      </DataTable>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import DataTable from "primevue/datatable";
import Column from "primevue/column";

const products = ref([]);

onMounted(async () => {
  try {
    const response = await fetch('http://localhost:8000/operadoras');
    const data = await response.json();
    products.value = data;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
});
</script>
