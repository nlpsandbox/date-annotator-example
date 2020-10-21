package org.openapitools.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import org.openapitools.jackson.nullable.JsonNullable;
import javax.validation.Valid;
import javax.validation.constraints.*;

/**
 * NoteAllOf
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2020-10-21T10:20:06.779899-07:00[America/Los_Angeles]")

public class NoteAllOf   {
  @JsonProperty("text")
  private String text;

  /**
   * The note type
   */
  public enum TypeEnum {
    PATHOLOGY("pathology"),
    
    PHONE_CALL("phone_call");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    @JsonValue
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    @JsonCreator
    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }
  }

  @JsonProperty("type")
  private TypeEnum type;

  public NoteAllOf text(String text) {
    this.text = text;
    return this;
  }

  /**
   * The content of the note
   * @return text
  */
  @ApiModelProperty(example = "On 09-03-1999, Ms Chloe Price met with Dr Joe.", value = "The content of the note")


  public String getText() {
    return text;
  }

  public void setText(String text) {
    this.text = text;
  }

  public NoteAllOf type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * The note type
   * @return type
  */
  @ApiModelProperty(value = "The note type")


  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
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
    NoteAllOf noteAllOf = (NoteAllOf) o;
    return Objects.equals(this.text, noteAllOf.text) &&
        Objects.equals(this.type, noteAllOf.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(text, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class NoteAllOf {\n");
    
    sb.append("    text: ").append(toIndentedString(text)).append("\n");
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

