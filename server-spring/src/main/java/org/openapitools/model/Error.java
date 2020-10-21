package org.openapitools.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import org.openapitools.jackson.nullable.JsonNullable;
import javax.validation.Valid;
import javax.validation.constraints.*;

/**
 * Error
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2020-10-21T10:20:06.779899-07:00[America/Los_Angeles]")

public class Error   {
  @JsonProperty("title")
  private String title;

  @JsonProperty("status")
  private Integer status;

  @JsonProperty("detail")
  private String detail;

  @JsonProperty("type")
  private String type;

  public Error title(String title) {
    this.title = title;
    return this;
  }

  /**
   * A human readable documentation for the problem type
   * @return title
  */
  @ApiModelProperty(required = true, value = "A human readable documentation for the problem type")
  @NotNull


  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }

  public Error status(Integer status) {
    this.status = status;
    return this;
  }

  /**
   * The HTTP status code
   * @return status
  */
  @ApiModelProperty(required = true, value = "The HTTP status code")
  @NotNull


  public Integer getStatus() {
    return status;
  }

  public void setStatus(Integer status) {
    this.status = status;
  }

  public Error detail(String detail) {
    this.detail = detail;
    return this;
  }

  /**
   * A human readable explanation specific to this occurrence of the problem
   * @return detail
  */
  @ApiModelProperty(value = "A human readable explanation specific to this occurrence of the problem")


  public String getDetail() {
    return detail;
  }

  public void setDetail(String detail) {
    this.detail = detail;
  }

  public Error type(String type) {
    this.type = type;
    return this;
  }

  /**
   * An absolute URI that identifies the problem type
   * @return type
  */
  @ApiModelProperty(value = "An absolute URI that identifies the problem type")


  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Error error = (Error) o;
    return Objects.equals(this.title, error.title) &&
        Objects.equals(this.status, error.status) &&
        Objects.equals(this.detail, error.detail) &&
        Objects.equals(this.type, error.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(title, status, detail, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Error {\n");
    
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    detail: ").append(toIndentedString(detail)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}

